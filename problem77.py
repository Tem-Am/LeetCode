class Solution:
    def combine(self, n: int, k: int):
        # two numbers: all possible comb of k from range in n
        # k  = 3 and n = 2; k = [1,1]; [2,1]; [3,1]; [4,1]; ...
        # all comb means that it is backtracking 
        # n = [ 1, 2,3, 4, ...]

        # make the array of numbers from the n first 
        comb = []
        def backtrack(index ,path): # add something here 
            if len(path) == k:
                comb.append(path[:]) # add to combinations 
                return #return null
            
            for i in range(index, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop() # pop from the top/latest item from the path

        backtrack(1, [])
        return comb    
