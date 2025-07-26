class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case
        if len(nums) == 1:
            return [[nums[0]]]

        # It is backtracking: returning all possible combinations
        permut = [] # this is possible permutations
        used = set()  # this used for know which interger is used since all integreg are differnt
        def backtrack(used, path):
            # when path includes all 
            if len(path) == len(nums): # all know all path has equal number of nums
                print(permut)
                permut.append(path[:])

            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                # if num is not used, add to used
                used.add(nums[i])
                path.append(nums[i]) # then expand path by num 
                backtrack(used, path) # call function again for next num
                used.remove(nums[i]) # after it has all numbers, return last element from used
                path.remove(nums[i]) # also remove last elemt from the path too see new path

        backtrack(used, [])
        return permut
