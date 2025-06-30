class Solution:
    def threeSum(self, nums: List[int]):
        ans = []
        # Sort first the array
        nums.sort()
        dupli = []

        for i in range(len(nums)):
            num1 = nums[i]
            # Check tow side of array to faster
            left = i + 1
            right = len(nums)-1
            if i == 0 or num1 != nums[i-1]:
                while left < right:
                    if nums[left] + nums[right] > -num1:
                        right -= 1
                    elif nums[left] + nums[right] < -num1:
                        left += 1
                    else:
                        ans.append([num1, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left-1] == nums[left]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        return ans