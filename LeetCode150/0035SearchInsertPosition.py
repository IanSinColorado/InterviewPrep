class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = int(len(nums) / 2)
        l = 0
        r = len(nums)

        while l < r:
            if target > nums[mid]:
                l = mid + 1
                mid = int((r-l)/2)
            else:
                r = mid - 1
                mid = int((r-l)/2)
        
        return r
