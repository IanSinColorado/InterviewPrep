class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()

        l = 0
        r = (position[-1] - position[0]) // (m-1)
        ans = 1

        while l <= r:
            mid = l + (r - l) // 2
            if self.isOkayAtDis(mid, position, m):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1


        return ans

    def isOkayAtDis(self, mid, position, m):
        countBallsPlaced = 1
        prevId = 0

        for i in range(1, len(position)):
            if (position[i]-position[prevId]) >= mid:
                countBallsPlaced += 1
                prevId = i
            if countBallsPlaced >= m:
                return True

        return False