class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # loop from col 
        # Change one number each time 
        # Switch each number from two sides acording to the diagnal
        x = 0
        y = 0
        while x < n or y < n:
            # First add one on each x and y coordinates
            # Then increament x and y by one. 
            # If it is more then half, decrement by one
            for inc in range(x+1, n):
                temp = matrix[inc][y]
                matrix[inc][y] = matrix[x][inc]
                matrix[x][inc] = temp
            x += 1
            y += 1
        
        # Step2: switch rows of two side until them meet
        leftCol = 0
        rightCol = n-1
        while leftCol < rightCol:
            for i in range(n):
                temp = matrix[i][leftCol]
                matrix[i][leftCol] = matrix[i][rightCol]
                matrix[i][rightCol] = temp
            leftCol += 1
            rightCol -=1 
        