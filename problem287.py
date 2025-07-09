class Solution:
    def findDuplicate(self, nums: List[int]):
        # Have two pointer at two end points
        slow = nums[0]
        fast = nums[0]
        # Loop until they meet
        while True:
            # slow goes step by step
            slow = nums[slow]
            # fast goes two steps
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow