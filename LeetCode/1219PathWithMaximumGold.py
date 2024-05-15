class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        # returns a path cost sum
        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == 0:
                return 0

            answer = 0
            currGrid = grid[row][col]
            for i in range(len(dx)):
                newRow = row + dx[i]
                newCol = col + dy[i]
                grid[row][col] = 0
                answer = max(answer, currGrid + dfs(newRow, newCol))
                grid[row][col] = currGrid

            return answer
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] != 0):
                    ans = max(ans, dfs(i, j))


        return ans