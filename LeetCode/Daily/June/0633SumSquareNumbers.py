class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low = 0
        high = int(c ** (1/2))

        while low <= high:
            sum = (high * high) + (low * low)
            if sum == c:
                return True
            elif sum < c:
                low += 1
            else:
                high -= 1

        return False