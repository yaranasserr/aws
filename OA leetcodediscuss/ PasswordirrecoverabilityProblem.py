from sortedcontainers import SortedSet

def min_time_to_be_irrecoverable(password, attackOrder, m):
    n = len(password)
    time = 0
    flag = False
    result = 0
    attacked = SortedSet()

    for i in range(n):
        currentPos = attackOrder[i]

        # Get the ceiling (next higher) and floor (next lower) positions in the sorted set
        high = attacked.bisect_left(currentPos + 1)  # Ceiling equivalent
        low = attacked.bisect_right(currentPos - 1)  # Floor equivalent

        left = 0
        right = 0

        if low == 0 and high == len(attacked):  # Neither low nor high exist
            left = currentPos - 1
            right = n - currentPos
        elif low == 0:  # Only high exists
            left = currentPos - 1
            right = attacked[high] - currentPos - 1
        elif high == len(attacked):  # Only low exists
            left = currentPos - attacked[low - 1] - 1
            right = n - currentPos
        else:  # Both low and high exist
            left = currentPos - attacked[low - 1] - 1
            right = attacked[high] - currentPos - 1

        both = left * right
        result += left + right + both + 1
        time += 1

        if result >= m:
            print(time)
            flag = True
            break

        attacked.add(currentPos)

    if not flag:
        print(-1)

# Example usage:
attackOrder = [1, 2, 3]
password = "abe"
m = 1
min_time_to_be_irrecoverable(password, attackOrder, m)  # Output: 1

attackOrder = [2, 4, 1, 3]
password = "bcdb"
m = 10
min_time_to_be_irrecoverable(password, attackOrder, m)  # Output: 4
