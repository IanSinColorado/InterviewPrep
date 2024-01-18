class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # No division
        # After fully watching the video
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= prefix
            prefix *= nums[i]

        return output


        '''
        # After watching the video
        prefixArr = [1] * len(nums)
        postfixArr = [1] * len(nums)
        output = [1] * len(nums)

        counter = 0
        lenNums = len(nums)

        while counter != len(nums):
            if counter == 0:
                prefixArr[0] = nums[0]
            else:
                prefixArr[counter] *= prefixArr[counter - 1]

            if counter == (lenNums - 1):
                postfixArr[counter] = nums[counter]
            else:
                postfixArr[counter] *= postfixArr[counter + 1]

            counter += 1

        for i in range(lenNums):
            if i == (lenNums - 1):
                output[i] == prefixArr[i]
            else:
                output[i] = prefixArr[i] * postfixArr[i + 1]

        return output'''



'''
# Before watching non-code NeetCode solution
# https://www.youtube.com/watch?v=bNvIQI2wAjk
        retArr = [1] * len(nums)

        lSize = 0

        while lSize != len(nums):
            for i in range(len(nums) - 1, lSize, -1):
                retArr[lSize] *= nums[i]

            for i in range(lSize):
                retArr[lSize] *= nums[i]

            lSize += 1

        return retArr
'''