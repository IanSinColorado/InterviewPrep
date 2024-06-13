# Recursive with a "memo" or storage of best value for each number
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1] * (len(nums) + 1)

        def iterate(index):
            if index < 0:
                return 0
            if memo[index] >= 0:
                return memo[index]
            
            res = max(iterate(index - 2) + nums[index], iterate(index - 1))
            memo[index] = res
            return res
        return iterate(len(nums)-1)

# iterative by building from the bottom up
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1] * (len(nums) + 1)

        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            memo[i+1] = max(memo[i], memo[i-1] + nums[i])
        
        return memo[len(nums)]
    
# iterative, but no "memo" or storage of best move
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        prev1 = 0
        prev2 = 0

        for i in range(len(nums)):
            tmp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = tmp

        return prev1