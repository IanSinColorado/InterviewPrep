# Using Queues
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        i = 0
        pops = 0

        while len(friends) != 1:
            i = (i + k-1) % len(friends)
            friends.pop(i)
            pops += 1

        return friends[0]
    
from collections import *
# deque solution
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()

        for i in range(1, n+1):
            q.append(i)

        while len(q) > 1:
            for i in range(k-1):
                q.append(q.popleft())
            q.popleft()

        return q[0]

    


# Recursive Solution
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # O(n), O(n)

        def helper(n, k):
            if n == 1:
                return 0
            
            return (helper(n-1, k) + k) % n

        
        return helper(n-1, k) + 1
    

# Bottom-up iterative solution
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # O(n), O(1)
        res = 0

        for people in range(1, n+1):
            res = (res + k) % people

        return res + 1