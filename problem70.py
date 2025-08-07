class Solution:
    def climbStairs(self, n: int):
        # Dynamic --> change chance to get there everything time 
        # See adding one 
        steps = 0

        # Base cases:
        if n == 1:
            return 1
        if n == 2:
            return 2

        oneStep = 2 # 1 step back from current
        twoStep = 1 # 2 step back from current
        for i in range(2, n):
            currentStep = oneStep + twoStep # Current from previous two
            twoStep = oneStep # New 2 steps behind
            oneStep = currentStep # New 1 step behind
        return oneStep