class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # There will always be exactly one solution
        # Only adding up two numbers

        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i == j:
                    continue

                if (num1 + num2) == target:
                    return [i,j]
        return []

# From LeetCode Solutions
# Using complement and a hash table
'''
# Two-Pass Solution (make hash table then traverse it)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
'''

'''
# One-Pass Solution ()
'''

'''
# Two-Pointer Solution (left and right):
class Solution:
    def twoSum(nums, target):
        numsWithIndex = [(num, i) for i, num in enumerate(nums)]
        print(numsWithIndex)
        numsWithIndex.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            num_sum = numsWithIndex[left][0] + numsWithIndex[right][0]
            if num_sum == target:
                return [numsWithIndex[left][1], numsWithIndex[right][1]]
            elif num_sum < target:
                left += 1
            else:
                right -= 1
        return []  # No solution found!
'''