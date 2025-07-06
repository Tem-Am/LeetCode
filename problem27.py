class Solution:
    def removeDuplicates(self, nums: List[int]):
        # Return only number
        # total number of dupli
        if len(nums) == 1:
            return 1
        elif len(nums) == 0:
            return 0
        
        newArray = []
        for i in range(len(nums)):
            # Need the first one 
            if i == 0:
                newArray.append(nums[i])
            else:
                if nums[i] != nums[i-1]:
                    newArray.append(nums[i])
        #Change nums array with no duplicates

        for j in range(len(newArray)):
            nums[j] = newArray[j]
        
        return len(newArray)

    def ChatSolution(nums):
        # If there is no element, return empty 
        if not nums:
            return 0
        # This is number of unique numbers in list
        i = 0
        
        for j in range(1, len(nums)):
            # If next number is different than unique number
            if nums[j] != nums[i]:
                # Increase number of unique number
                i += 1
                # Change number unique into nums list
                nums[i] = nums[j]        
        return i + 1

