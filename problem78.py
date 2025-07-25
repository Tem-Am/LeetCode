class Solution:
    def subsets(self, nums):
        # Back Tracking problem
        # Base case:
        if len(nums) == 1:
            return [[], [nums[0]]]

        # No need to work on backtracking algorithm 
        # Recursive: what condition: when it has all number, pop or go back 
        subsets = []
        def backtrack(start, path):
            # Add to subset
            subsets.append(path[:])
            for i in range(start, len(nums)):
                # add num to path
                path.append(nums[i])
                # Call it recursively 
                backtrack(i+1, path)
                # Backtrack
                path.pop()
        print(subsets, "why")
        backtrack(0, [])
        