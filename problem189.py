class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Base case
        if k % len(nums) == 0:
            return nums
        # reverse
        
        # if k is greater than n
        k = k % len(nums)

        def reverse(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        
        # Step one reverse whole array
        reverse(0, len(nums)-1)
        print(nums)

        # Step2: reverse 0 to k
        reverse(0, k-1)
        print(nums)

        #Step3 : reverse  k to n
        reverse(k, len(nums)-1)
        print(nums)

