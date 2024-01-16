from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) == 1:
            return nums[0]
        
        counter = defaultdict(int)

        for i in nums:
            counter[i] += 1

        counterTuple = list()

        for key, value in counter.items():
            counterTuple.append((value, key))

        counterTuple = sorted(counterTuple, reverse=True)

        retList = []
        for i in range(k):
            retList.append(counterTuple[i][1])

        return retList

