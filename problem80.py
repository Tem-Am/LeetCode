class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # run all the way 
        length = 1
        k = 0
        index = 0
        for i in range(len(nums)-1):
            if length < 3:
                nums[index] = nums[i]
                index += 1
            if nums[i] == nums[i+1]:
                length += 1
            else:
                if length >= 2:
                    k += 2
                else:
                    k += 1
                length = 1
        if length == 1:
            k += 1
        else:
            k += 2
        nums[k-1] = nums[len(nums)-1]
        return k
