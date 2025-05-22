# The Amazon Alexa development team needs to analyze request logs across numSkills different Alexa skills to understand their performance and user engagement.

# The skills are indexed from 1 to numSkills, and the logs are provided as a 2D array requestLog of size m where requestLog[i] = [skill_ID, timeStamp] represents a request made at timeStamp to the skill with ID skill_ID.

# You are given an integer numSkills, a 2D integer array requestLogs, an integer timeWindow (representing a lookback period), and an array of queryTimes containing q queries.

# For each queryTime[i] determine the number of skills that did not receive a request in the time interval [queryTime[i] - timeWindow, queryTime[i]]. Return an array of length q containing the result of each of the query.

# Note: If for some query in the numSkills received requestLog the given time interval for that query, then answer is 0.

# Function Description

# Complete the function findIdleSkillsQuery in the editor.

# findIdleSkillsQuery has the following parameters:

# 1. int numSkills: an integer denoting the number of skills
# 2. int[][] requestLogs: 2D array denoting the request logs
# 3. int[] queryTime: an integer array denoting the query times
# 4. int timeWindow: an integer denoting the lookback period for queries
# Returns

# int[]: an integer array denoting the answers to the queries

# 🌷 A super special thanks to an old friend who kindly helped out! 🌷

# Example 1:

# Input:  numSkills = 3, requestLogs = [[1, 3], [2, 6], [1, 5]], queryTime = [10, 11], timeWindow = 5
# Output: [1, 2] 
# Explanation:

# For queryTime[0] = 10, skills 1 and 2 had requests at timeStamps 5 and 6, respectively,  which fall in the interval [5, 10]. Skill 3 did not receive any requests in the given interval. Thus, answer for this queryTime is 1.

# For queryTime[1] = 11, skill 2 requests at timeStamp6, respectively, which fall in the interval [6, 11]. Skill 1 and 3 did not receive any requests in the given interval. Thus, answer for this queryTime is 2.

# So, our answer turns out to be [1, 2].
      
      
# Example 2:

# Input:  numSkills = 6, requestLogs = [[3, 2], [4, 3], [2, 6], [6, 3]], queryTime = [3, 2, 6], timeWindow = 2
# Output: [3, 5, 5] 
# Explanation:

# For queryTimes[0] = 3, in time interval [1, 3] skills [3, 4, 6] receives requests.

# For queryTime [1] = 2, in time interval [0, 2] skills [3] receives requests.

# For queryTime [2] = 6, in time interval [4, 6] skills [2] receives requests.
      
      
# Example 3:

# Input:  numSkills = 6, requestLogs = [[3, 2], [4, 3], [2, 6], [6, 3]], queryTime = [1, 2, 3, 4, 5, 6], timeWindow = 1
# Output: [6, 5, 3, 4, 6, 5] 
# Explanation:

# ~o~   


import unittest
from typing import List

class YourClassName:
    def findIdleSkillsQuery(self, numSkills: int, requestLogs: List[List[int]], queryTime: List[int], timeWindow: int) -> List[int]:
        res = []
        for endTime in queryTime:
            beginTime = max(endTime - timeWindow, 0)
            
            # Track which skills had requests in [beginTime, endTime]
            active_skills = set()
            
            for skill_id, timestamp in requestLogs:
                if beginTime <= timestamp <= endTime:
                    active_skills.add(skill_id)
            
            # idle skills = total skills - skills that had requests
            idle_count = numSkills - len(active_skills)
            res.append(idle_count)
        
        return res

# Unit test class stays the same
class TestFindIdleSkillsQuery(unittest.TestCase):
    def setUp(self):
        self.obj = YourClassName()

    def test_example_1(self):
        numSkills = 3
        requestLogs = [[1, 3], [2, 6], [1, 5]]
        queryTime = [10, 11]
        timeWindow = 5
        expected = [1, 2]
        result = self.obj.findIdleSkillsQuery(numSkills, requestLogs, queryTime, timeWindow)
        self.assertEqual(result, expected)

    def test_example_2(self):
        numSkills = 6
        requestLogs = [[3, 2], [4, 3], [2, 6], [6, 3]]
        queryTime = [3, 2, 6]
        timeWindow = 2
        expected = [3, 5, 5]
        result = self.obj.findIdleSkillsQuery(numSkills, requestLogs, queryTime, timeWindow)
        self.assertEqual(result, expected)

    def test_example_3(self):
        numSkills = 6
        requestLogs = [[3, 2], [4, 3], [2, 6], [6, 3]]
        queryTime = [1, 2, 3, 4, 5, 6]
        timeWindow = 1
        expected = [6, 5, 3, 4, 6, 5]
        result = self.obj.findIdleSkillsQuery(numSkills, requestLogs, queryTime, timeWindow)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
