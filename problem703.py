class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binaray seach
        # Divide problem into two
        def divide(number, left, right, target):
            if left > right:
                return -1
            mid = (right - left)//2 + left # find the middle point
            if number[mid] == target:
                return mid
            elif number[mid] > target:
                return divide(number,left, mid-1, target) # check in the left side
            elif number[mid] < target: # check in the right side
                 return divide(number, mid+1, right, target)
        return divide(nums, 0, len(nums) -1, target)