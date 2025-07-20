import List
class Solution:
    def jump(self, nums: List[int]):
        # Base case
        if len(nums) == 1:
            return 0
        steps = 0
        farthest = 0 # farthest jump from current index
        end = 0 # end of current jump
        # Save concept
        # Greedy to reach final distition with least steps
        for i in range(len(nums)-1):
            farthest = max( farthest, i + nums[i])

            # we will increase the number of step, we reach the end of current possible step
            # then we reach the end, we know the farthest step for next step.
            if i == end:
                steps += 1
                end = farthest
        return steps