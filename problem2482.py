class Solution:
    def onesMinusZeros(self, grid: List[List[int]]):
        # creaate matrxi diff   
        diff = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        # run it first time for all col value
        listcols = []
        for row in range(len(grid)):
            val = 0
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    val += 1
                else:
                    val -= 1
            listcols.append(val)
        listrow = []
        for col in range(len(grid[0])):
            val = 0
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    val += 1
                else:
                    val -= 1
            listrow.append(val)

        for row in range(len(diff)):
            for col in range(len(diff[0])):
                diff[row][col] = listcols[row] + listrow[col]
        return diff 