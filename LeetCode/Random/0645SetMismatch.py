from collections import defaultdict

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0] * 2
        counter = defaultdict(int)
        numsSet = set(nums)
        allNums = set(range(1, len(nums) + 1))

        # print(numsSet)
        # print(allNums)

        for num in nums:
            counter[num] += 1

        output[0] = counter.keys()[counter.values().index(2)]
        output[1] = (allNums - numsSet).pop()

        return output