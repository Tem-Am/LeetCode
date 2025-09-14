class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]):
        # It is dp problem 
        # From bot to top

        for row in range(len(matrix)-1, 0, -1):
            # there are two options for next number 
            # first one is when it is two end of row
            for col in range(len(matrix)):
                if col == 0:
                    matrix[row-1][col] += min(matrix[row][col], matrix[row][col+1])
                elif col == len(matrix)-1:
                    matrix[row-1][col] += min(matrix[row][col-1], matrix[row][col])
                else:
                    matrix[row-1][col] += min(matrix[row][col-1], matrix[row][col], matrix[row][col+1])
        
        return min(matrix[0])