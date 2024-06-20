# Using Sorting
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))
        
        res = i = best = 0

        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            res += best
        
        return res


# Using a best profit so far scheme
# Then go up the list and fill in the best one, to overlap any low profits with high difficulity
# Go through the worker difficulity and add up the best jobs
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        maxDifficulty = max(difficulty)
        maxProfitForDifficulty = [0] * (maxDifficulty+1)

        for i in range(len(difficulty)):
            maxProfitForDifficulty[difficulty[i]] = max(maxProfitForDifficulty[difficulty[i]], profit[i])

        for i in range(1, maxDifficulty+1):
            maxProfitForDifficulty[i] = max(maxProfitForDifficulty[i], maxProfitForDifficulty[i-1])

        res = 0
        for i in range(len(worker)):
            if worker[i] > maxDifficulty:
                res += maxProfitForDifficulty[maxDifficulty]
            else:
                res += maxProfitForDifficulty[worker[i]]

        return res