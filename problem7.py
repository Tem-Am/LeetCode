# Reverse Integer 

class Solution:
    def reverse(self, x: int):
        # First, convert into string to easily reverse the number
        stringVersion = str(x)
        # Check number is negative or possitive
        if stringVersion[0] != "-":
            reversedString = stringVersion[::-1]
            index = 0
            while reversedString[index] == 0:
                index += 1
            reversedInt = int(reversedString[index::])
        else:
            stringVersion = stringVersion[1::]
            reversedString = stringVersion[::-1]
            index = 0
            while reversedString[index] == 0:
                index += 1
            reversedInt =  int('-'+reversedString[index::])
        # Check boundries
        # If the number is out of range, we will return 0
        if 2 ** 31 - 1 < reversedInt or -( 2 ** 31) > reversedInt:
            return 0
        else:
            return reversedInt
    
    def gptSolution(self, x: int):
        # Check the sign 
        sign =  -1 if x < 0 else 1
        
        # Get the absolute value of x
        x = abs(x)
        # Finall reversed number
        res = 0
        while x != 0:
            # Get the last number of x
            pop = x %10
            
            # Divide by 10 
            x = x //10
            
            # Check overflow before multiplying and adding
            if res > (2**31 - 1) // 10 or (res == (2**31 -1 ) // 10 and pop > 7):
                return 0
            res = res * 10 + pop
        
        return res * sign