##########
# String into Integer
# MY code:
##########

def numfunc(n : str):
        if n == "0":
            return 0
        elif n == "1":
            return 1
        elif n == "2":
            return 2
        elif n == "3":
            return 3
        elif n == "4":
            return 4            
        elif n == "5":
            return 5
        elif n == "6":
            return 6
        elif n == "7":
            return 7
        elif n == "8":
            return 8
        elif n == "9":
            return 9
        # Means that it is not a number
        else:
            return 10

class Solution:
    def myAtoi(self, s: str):
        # Loop until get the answer
        number = 0
        # They are flages for knowing first time 
        whitespace = 0
        signedness = 0
        conversion = 0
        sign = 1
        for l in s:
            if numfunc(l) == 10:
                if signedness == 1 or whitespace == 1:
                    if number * sign > 2 ** 31 -1:
                        return 2 ** 31 - 1
                    elif number * sign < -(2 ** 31):
                        return -(2 ** 31)
                    else:
                        return number * sign
                if l == "-":
                    sign = -1
                    signedness = 1
                elif l == "+":
                    sign = 1
                    signedness = 1
                elif l == " ":
                    0 == 0
                # If char is not number or sign or whitespace, it means that we need return it. 
                else:
                    if number * sign > 2 ** 31 -1:
                        return 2 ** 31 - 1
                    elif number * sign < -(2 ** 31):
                        return -(2 ** 31)
                    else:
                        return number * sign
            else:
                if number > (2**31-1)//10:
                    return 2 ** 31 - 1 if sign == 1 else -2**31
                if signedness != 0:
                    print(signedness)
                    signedness = signedness
                else:
                    signedness = 1
                num = numfunc(l)
                number = number*10 + num 
                
        # If it read until the end of string
        if number * sign > 2 ** 31 -1:
            return 2 ** 31 - 1 
        elif number * sign < -(2 ** 31):
            return -(2 ** 31)
        else:
            return number * sign
                
                
#####################
## 
## ChatGPT FSM solution:
#####################
class Solution:
    def myAtoi(self, s: str):
        state = 'start'
        sign = 1
        number = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        def transition(ch):
            if ch == ' ':
                return 'start'
            elif ch in '+-':
                return 'signed'
            elif ch.isdigit():
                return 'in_number'
            else:
                return 'end'

        i = 0
        while i < len(s):
            ch = s[i]
            new_state = transition(ch)

            if state == 'start':
                if new_state == 'signed':
                    sign = -1 if ch == '-' else 1
                    state = 'signed'
                elif new_state == 'in_number':
                    number = int(ch)
                    state = 'in_number'
                elif new_state == 'end':
                    break
            elif state == 'signed':
                if new_state == 'in_number':
                    number = int(ch)
                    state = 'in_number'
                else:
                    break
            elif state == 'in_number':
                if new_state == 'in_number':
                    digit = int(ch)
                    if number > (INT_MAX - digit) // 10:
                        return INT_MAX if sign == 1 else INT_MIN
                    number = number * 10 + digit
                else:
                    break

            i += 1

        return number * sign
