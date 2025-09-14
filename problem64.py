class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        # Fill the first row (can only come from the left)
        for col in range(1, m):
            grid[0][col] += grid[0][col - 1]

        # Fill the first column (can only come from above)
        for row in range(1, n):
            grid[row][0] += grid[row - 1][0]

        # Fill the rest of the grid
        for row in range(1, n):
            for col in range(1, m):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])

        return grid[n - 1][m - 1]