class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        # it is multi-source bfs where we need to find all rotten oranges first 

        n = len(grid)
        m = len(grid[0])
        numberOfOrange = 0
        q = deque()
        visited = set()

        # To find find initial rotten oranges first 
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    q.append((row,col))
                    visited.add((row,col))

                # To know how many fresh orange is there
                if grid[row][col] == 1:
                    numberOfOrange += 1

        # Edge case
        if len(q) == 0 and numberOfOrange == 0:
            return 0
        minute = -1
        # No time to use bfs
        while q:
            length = len(q)
            while length > 0:
                r, c = q.popleft()
                if r + 1 < n and (r+1,c) not in visited:
                    if grid[r+1][c] == 1:
                        numberOfOrange -= 1
                        q.append((r+1,c))
                        visited.add((r+1,c))
                if r - 1 > -1 and (r-1,c) not in visited:
                    if grid[r-1][c] == 1:
                        numberOfOrange -= 1
                        q.append((r-1,c))
                        visited.add((r-1,c))
                if c + 1 < m and (r,c+1) not in visited:
                    if grid[r][c+1] == 1:
                        numberOfOrange -= 1
                        q.append((r,c+1))
                        visited.add((r,c+1))
                if c - 1 > -1 and (r,c-1) not in visited:
                    if grid[r][c-1] == 1:
                        numberOfOrange -= 1
                        q.append((r,c-1))
                        visited.add((r,c-1))
                length -= 1
            minute += 1
        if numberOfOrange != 0:
            return -1

        return minute