import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # check four sides ot for faster result 
        top1 = [0,0]
        top2 = [0, len(matrix[0])-1]
        bot1 = [len(matrix)-1, 0]
        bot2 = [len(matrix)-1, len(matrix[0])-1]
        # Run until they meet
        zerosIndexs = {}
        while top1[0] <= bot1[0]:
            top1[1] = 0
            top2[1] = len(matrix[0])-1
            bot1[1] = 0
            bot2[1] = len(matrix[0])-1
            while top1[1] <= top2[1]:
                if matrix[top1[0]][top1[1]] == 0:
                    zerosIndexs[top1[0],top1[1]] = 1
                if matrix[top2[0]][top2[1]] == 0:
                    zerosIndexs[top2[0], top2[1]] = 1
                if matrix[bot1[0]][bot1[1]] == 0:
                    zerosIndexs[bot1[0], bot1[1]] = 1
                if matrix[bot2[0]][bot2[1]] == 0:
                    zerosIndexs[bot2[0], bot2[1]] = 1
                top1[1] += 1
                top2[1] -= 1
                bot1[1] += 1
                bot2[1] -=1
            top1[0] += 1
            top2[0] += 1
            bot2[0] -= 1
            bot1[0] -= 1

        for key in zerosIndexs:
            # Make all row to zeros
            for i in range(len(matrix[0])):
                matrix[key[0]][i] = 0
            # make all col to zeros
            for j in range(len(matrix)):
                matrix[j][key[1]] = 0
        print(matrix)
