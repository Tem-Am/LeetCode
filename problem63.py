class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid): 
        # DP problem where moves only left and right 
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        # For first row of grid, we can move only direction(right)
        index = 0
        while index < n and obstacleGrid[index][0] != 1:
            obstacleGrid[index][0] = 2
            index += 1
       
        # For first col of grid, we can move only one direction(down)
        index2 = 0
        while index2 < m and obstacleGrid[0][index2] != 1:
            obstacleGrid[0][index2] = 2
            index2 += 1

        for row in range(1, n):
            for col in range(1,m):
                if obstacleGrid[row][col] != 1:
                    if obstacleGrid[row-1][col] != 1:
                        obstacleGrid[row][col] += obstacleGrid[row-1][col]
                    if obstacleGrid[row][col-1] != 1:
                        obstacleGrid[row][col] += obstacleGrid[row][col-1]

        return obstacleGrid[n-1][m-1]//2