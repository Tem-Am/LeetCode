class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        # backtracikng becasue return all possible combinations
        # start with empty array 
        # [] -> add all numbers one by one 
        # Global sum and comb where is collect current sum and answer list
        
        ans = [] # if sum match add here
        indexAns = []
        def bkt(current, indexs):
            if sum(current) == target:
                temp = indexs[:]
                temp.sort()
                if temp not in indexAns:
                    indexAns.append(temp[:])
                    ans.append(current[:]) # we will add to ans
                return # return nothing 
            if sum(current) > target:
                return
            for i in range(len(candidates)):
                current.append(candidates[i]) # add to list 
                indexs.append(i)
                bkt(current, indexs) # call it recursively 
                current.pop()
                indexs.pop()
        bkt([], [])
        return ans