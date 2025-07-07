class Solution:
    def fourSum(self, nums: List[int], target: int):
        if len(nums) < 4:
            return []
        # Number recursive problem 
        # Sort the list
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j+1
                right = len(nums)-1
                newtarget = target - nums[i] - nums[j]
                # New targat with finding two numbers from list 
                while left < right:
                    twosum = nums[left] + nums[right]
                    if twosum > newtarget:
                        right -= 1
                    elif twosum < newtarget:
                        left += 1
                    else:
                        if [nums[i],nums[j], nums[left], nums[right]] not in ans:
                            ans.append([nums[i],nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
        return ans