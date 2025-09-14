class Solution:
    def mySqrt(self, x: int):
        # Base CAse
        if x == 0:
            return 0
        if x < 4:
            return 1
        # Narrow down into number
        for i in range(1, x//2+2):
            if i * i == x:  
                return i
            elif i*i > x:
                return i-1
