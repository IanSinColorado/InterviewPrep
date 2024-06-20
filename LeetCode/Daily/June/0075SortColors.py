# My Own solution!
# Two pass: First make the hash, then use it to make the array
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        from collections import defaultdict

        hash = defaultdict(int)
        for i in range(n):
            hash[nums[i]] += 1

        count = 0
        for i in range(4):
            while hash[i] != 0:
                nums[count] = i
                count += 1
                hash[i] -= 1



# Dutch - Three-way partitioning
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else: 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

