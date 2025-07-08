class Solution:
    def productExceptSelf(self, nums: List[int]):
        # Total pre and suffix product of all numbers in nums
        PreTotal = 1   
        SufTotal = 1
        # answer list 
        answer = []   
        # Loop for find total product without 0s in array
        pre = [1]
        suf = [1]
        indexRev = len(nums)-1
        for i in range(1, len(nums)):
            PreTotal *= nums[i-1]
            pre.append(PreTotal)
            SufTotal *= nums[indexRev]
            suf.append(SufTotal)
            indexRev -= 1
        suf.reverse()
        # if there is more than one zero, all product will be 0
        for j in range(len(nums)):
            answer.append(pre[j]*suf[j])

        return answer