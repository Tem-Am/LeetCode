# Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int):
        # Used the sequence on each row
        # There is sequence of increasing next letter from the string
        # N and M are sequence: It starts with N is 2*(numRows-1) and M is 2*0
        # Then, each of them are decreased and added by 1.
        
        # If number of rows is 1, return exact string
        if numRows == 1 or numRows >= len(s):
            return s
        else:
            newWord = []
            for i in range(numRows):
                n = 2*(numRows - (i+1))
                m = 2 *(i)
                # Temp variable is for adding each letter from string into our answer until it reaches length of s.
                temp = i
                # Switch is for switching N and M to add to temp
                switch = 0
                while temp < len(s):
                    if switch == 0:
                        if n != 0:
                            newWord.append(s[temp])
                            temp += n
                        switch = 1
                    else:
                        if m != 0:
                            newWord.append(s[temp])
                            temp += m
                        switch = 0
            return ''.join(newWord)
        
        
###################
## ChatGpt Solution
##################

    def gptSolution(s: str, numRows: int):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows =  [''] * numRows
        current_row = 0
        going_down = False
        
        for l in s:
            rows[current_row] += l
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return ''.join(rows)