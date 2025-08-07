class Solution:
    def numIslands(self, grid: List[List[str]]):
        # find cluster of 1 in map
        # depth first search 

        # dfs return x and y when it cannot find one other 1s
        # means that island increased by one
        visited = set()
        path = []
        def dfs(row, col):
            # check the top 
            if row > 0 and grid[row-1][col] == "1" and (row-1, col) not in visited:
                visited.add((row-1, col))    
                dfs(row-1, col)
            # check right 
            if col < len(grid[0])-1 and grid[row][col+1] == "1" and (row, col+1) not in visited: 
                visited.add((row, col+1))    
                dfs(row,col+1)
            # check bottom 
            if row < len(grid)-1 and grid[row+1][col] == "1" and (row+1, col) not in visited: 
                visited.add((row+1, col))    
                dfs(row+1, col)
            # check left 
            if col > 0 and grid[row][col-1] == "1" and (row, col-1) not in visited: 
                visited.add((row, col-1))    
                dfs(row, col-1)
            
        island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    dfs(r,c)
                    island += 1
        return island