#################
## Container with most water
##################

class Solution:
    def maxArea(self, height: List[int]):
        # Two point of list 
        start = 0
        end = len(height)-1
        # The initial value of space is 0
        maxWater = 0
        # Loop until two end points meet
        while start < end:
            if height[start] <= height[end]:
                temp = height[start] * (end - start)
                start += 1
            else:
                temp = height[end] * (end -start)
                end -= 1
            if maxWater < temp:
                maxWater = temp
        return maxWater