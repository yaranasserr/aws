class RegexSolver:
    def findLongestRegex(self, x: str, y: str, z: str) -> str:
    
        if y == z:
            return "-1"
        if len(x) != len(y):
            return "-1"
        
        n = len(x)
        z_len_match = (len(z) == n)
        
        # Check if it's possible to exclude z
        can_exclude_z = not z_len_match
        exclude_pos = -1
        if z_len_match:
            for i in range(n):
                a, b, c = x[i], y[i], z[i]
                if a == b:
                    if c != a:
                        can_exclude_z = True
                        exclude_pos = i
                        break
                else:
                    if c != a and c != b:
                        can_exclude_z = True
                        exclude_pos = i
                        break
            if not can_exclude_z:
                return "-1"
        
        regex_parts = []
        for i in range(n):
            a, b = x[i], y[i]
            if a == b:
                part = f"[{a}]"
            else:
                chars = [a, b]
                chars.sort()
                part = f"[{''.join(chars)}]"
            regex_parts.append(part)
        
        # Verify that the constructed regex excludes z if needed
        if z_len_match:
            matched = True
            for i in range(n):
                c = z[i]
                part = regex_parts[i]
                if part.startswith('['):
                    chars = part[1:-1]
                    if c in chars:
                        continue
                    else:
                        matched = False
                        break
                else:
                    if c == part:
                        continue
                    else:
                        matched = False
                        break
            if matched:
                return "-1"
        
        return ''.join(regex_parts)
import unittest

class TestFindLongestRegex(unittest.TestCase):
    def setUp(self):
        self.solver = RegexSolver()

    def test_case_1(self):
        x = "AB"
        y = "BD"
        z = "CD"
        expected = "[AB][BD]"
        result = self.solver.findLongestRegex(x, y, z)
        self.assertEqual(result, expected)

    def test_case_2(self):
        x = "AERB"
        y = "ATRC"
        z = "AGCB"
        expected = "[A][ET][R][BC]"
        result = self.solver.findLongestRegex(x, y, z)
        self.assertEqual(result, expected)

    def test_case_3(self):
        x = "ABCD"
        y = "CODE"
        z = "CODE"
        expected = "-1"
        result = self.solver.findLongestRegex(x, y, z)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
