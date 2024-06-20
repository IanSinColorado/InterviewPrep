class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        total = 0
        size = 1
        while size < len(nums):
            l, r = 0, len(nums)
            count = 0

            while l < len(nums)-1:
                xorNum = nums[l]
                i = l+1
                count = 1
                while i <= len(nums)-1 and count < size:
                    count += 1
                    i += 1
                    xorNum = xorNum ^ nums[i]

                total += xorNum
                l += 1
            size += 1

        return total