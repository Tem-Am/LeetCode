class Solution:
    def updateMatrix(self, mat: List[List[int]]):        
        # bfs for all 0s first and expand from there 
        row = len(mat)
        col = len(mat[0])

        # Base case
        if row == 1 and col == 1:
            return mat
            
        # find all 0s first 
        q = deque()
        visited = set()
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        # Run until all the queue
        while q:
            path = q.popleft()
            r = path[0]
            c = path[1]

            if c-1 > -1 and (r,c-1) not in visited:
                q.append([r, c-1])
                visited.add((r, c-1))
                mat[r][c-1] = mat[r][c] + 1
            if c+1 < col and (r, c+1) not in visited:
                q.append([r, c+1])
                visited.add((r, c+1))
                mat[r][c+1] = mat[r][c] + 1
            if r+1 < row and (r+1, c) not in visited:
                q.append([r+1, c])
                visited.add((r+1, c))
                mat[r+1][c] = mat[r][c] + 1
            if r-1 > -1 and (r-1, c) not in visited:
                q.append([r-1, c])
                visited.add((r-1, c))
                mat[r-1][c] = mat[r][c] + 1
        
        return mat
            