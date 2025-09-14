class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Go through all the rows 
        # Choose smaller number from index i or i + 1

        # Base case
        if len(triangle) == 1:
            return triangle[0][0]

        # Dynamic programming 
        # Changable variables for sum of numbers and index 

        for row in range(len(triangle)-1, 0, -1):
            # Start from bottom to top
            # Update second to last row 
            # For each node, add min number of two numbers
            for col in range(len(triangle[row])-1):
                # Update row above
                triangle[row-1][col] += min(triangle[row][col], triangle[row][col+1])
                
        return triangle[0][0]