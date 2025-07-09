import List

class Solution:
    def missingNumber(self, nums: List[int]):
        # Know that max number will be N or N-1 
        # Find the total sum of each number and substract from the sum of list
        totalSum = 0
        for i in range(len(nums)+1):
            totalSum += i

        listSum = 0
        for j in nums:
            listSum += j

        return totalSum-listSum