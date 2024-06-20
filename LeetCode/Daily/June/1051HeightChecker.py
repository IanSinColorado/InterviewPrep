class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # use a good sorting technique
        sort = sorted(heights)

        wrong = 0
        for i in range(len(heights)):
            if heights[i] != sort[i]:
                wrong += 1

        return wrong