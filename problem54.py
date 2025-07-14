import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]):
        # Two pointer 
        # One is goes to left and right direction
        # Other is for up and down
        # After all m is done, it is done 
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        newMat = [[0 for _ in range(cols)] for _ in range(rows)]
        # Dirs goes left and right in matrix
        dirs = 0 
        # upDown goes through rows
        upDown = 0

        while newMat[upDown][dirs] != 1:
            # If newMat is all 1, it means that all path is done
            if dirs < cols - 1 and newMat[upDown][dirs+1] == 0:
                while dirs < cols - 1 and newMat[upDown][dirs+1] == 0:
                    newMat[upDown][dirs] = 1
                    ans.append(matrix[upDown][dirs])
                    dirs += 1
            elif upDown < rows-1 and newMat[upDown+1][dirs] ==0:
                while upDown < rows-1 and newMat[upDown+1][dirs] ==0:
                    newMat[upDown][dirs] = 1
                    ans.append(matrix[upDown][dirs])
                    upDown += 1
            elif dirs > 0 and newMat[upDown][dirs-1] == 0:
                while dirs > 0 and newMat[upDown][dirs-1] == 0:
                    newMat[upDown][dirs] = 1
                    ans.append(matrix[upDown][dirs])
                    dirs -= 1
            elif upDown > 0 and newMat[upDown-1][dirs] == 0:
                while upDown > 0 and newMat[upDown-1][dirs] == 0:
                    newMat[upDown][dirs] = 1
                    ans.append(matrix[upDown][dirs])
                    upDown -= 1
            else:
                newMat[upDown][dirs] = 1
                ans.append(matrix[upDown][dirs])
        return ans
    
    def ChatSolu(self, matrix: List[List[int]]):
        # Use four indexs for diretions
        # Initial point of all direction
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        
        ans = []
        while left <= right and bottom <= top:
            
            # Goes left to right 
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            
            for j in range(top, bottom+1):
                ans.append(matrix[j][right])
            right  -= 1
            
            if top <= bottom:
                # Goes right to left
                for i in range(right, left -1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Goes up
                for j in range(bottom, top -1, -1):
                    ans.append(matrix[j][left])
                left += 1
        return ans