# # Original Solution
# # Runtime: 22 ms, beats 35%
# # Memory: 11.62 MB, beats 57%
# class Solution(object):
#     def flipRow(self, grid, row):
#         for i in range(len(grid[row])):
#             if grid[row][i] == 0:
#                 grid[row][i] = 1
#             else:
#                 grid[row][i] = 0
#         return grid

#     def flipColumn(self, grid, col):
#         newGrid = grid
#         for i in range(len(grid)):
#             if newGrid[i][col] == 0:
#                 newGrid[i][col] = 1
#             else:
#                 newGrid[i][col] = 0
#         return newGrid


#     def matrixScore(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         # get the most amount of 1s in the first spot
#         # get the most amount of 1s in second spot
#         m = len(grid)
#         n = len(grid[0])

#         for i in range(m):
#             if grid[i][0] == 0:
#                 self.flipRow(grid, i)

#         print(grid) 
#         for i in range(n):
#             count0 = 0
#             count1 = 0
#             for j in range(m):
#                 if grid[j][i] == 0:
#                     count0 += 1
#                 else:
#                     count1 += 1

#             if count0 > count1:
#                 print("True")
#                 print("i", i)
#                 print("j", j)
#                 grid = self.flipColumn(grid, i)
#             else:
#                 print("False")
#         if n > 1:
#             print(self.flipColumn(grid, 3))
#         self.flipColumn(grid, 0)
#         print(grid)
#         return 0 
    

# Greedy Solution Without Memory:
# Record whether the first column is a 1
# Go column by column and maximize the number of 1s
class Solution(object):
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])

        sum = m * (2 ** (n-1))

        for i in range(1, n):
            # each column
            colCount = 0
            for j in range(m):
                # each row of a column
                colCount += grid[j][0] ^ grid[j][i] # flip the digit if the first number in row is not a 1

            if colCount < (m-colCount):
                sum += (m-colCount) * 2 ** (n-i-1)
            else:
                sum += colCount * 2 ** (n-i-1)

        return sum