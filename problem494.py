class Solution:
    def findTargetSumWays(self, nums: List[int], target: int):
        # Base case 
        if len(nums) == 1:
            # Only case is when it is 0
            if -nums[0] == target and nums[0] == target:
                return 2
            elif nums[0] == target or -nums[0] == target:
                return 1
            else:
                return 0
        tree = [[0], []]
        # Add all numbers and change each number by multi by 1 and -1 
        # This is tree for all possible sum in the last node
        for num in nums:
            for leaf in tree[0]:
                tree[1].append(leaf+num)
                tree[1].append(leaf-num)
            # To save memory space, used only two lists            
            temp = tree[1]
            tree[0] = temp
            tree[1] = []
        output = 0
        # Now, we have all possible combination of sum 
        for sums in tree[0]:
            if sums == target:
                output += 1
        
        return output