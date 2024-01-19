class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # After viewing NeetCode youtube video and seeing the way it was written out in a tree-like way
        # No code was viewed for making this solution
        if n == 1:
            return 1

        if n == 2:
            return 2
        
        dp = [-1] * n

        dp[n - 1] = 1
        dp[n - 2] = 2

        for i in reversed(range(n - 2)):
            dp[i] = dp[i+1] + dp[i+2]

        return dp[0]