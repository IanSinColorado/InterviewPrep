# With a storage of all previous step sizes
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        storage = [-1] * (n + 1)

        def solver(n):
            if n == 1:
                return 1
            
            if n == 2:
                return 2
            
            out = 0
            if storage[n-1] == -1:
                out += solver(n-1)
            else:
                out += storage[n-1]

            if storage[n-2] == -1:
                out += solver(n-2)
            else:
                out += storage[n-2]

            storage[n] = out
            return out
        
        return solver(n)
    

# Only counting a previous step sum and second previous step sum
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        firstCounter = 1
        secondCounter = 2
        total = 0

        for i in range(2, n):
            total = firstCounter + secondCounter
            firstCounter = secondCounter
            secondCounter = total

        return total