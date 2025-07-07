class Solution:
    def isValid(self, s: str):
        # Priority is important to close in order
        # Some case no need to extra calculation
        # If there is odd number of string there is at least one that do not have 
        # close or open bracket
        if len(s) % 2 == 1:
            return False
        # Create stack for charecter
        # To be true it need to be empty
        stack = []
        for i in s:
            # Go througb stack from the top
            stack.append(i)
        opening = 0
        closing = 0
        index = 0
        while index < len(s) and len(stack) > 0:
            # If first item in stack is opening bracket 
            # We push them into top of stack
            # If it is close item, we match with top of stack
            # If they do not match return false
            if stack[0] == "(" or stack[0] == "{" or stack[0] == "[":
                stack.append(stack[0])
                stack.pop(0)
                opening += 1
            elif stack[0] == ")":
                if stack.pop() != "(":
                    return False
                else:
                    stack.pop(0)
                    closing += 1
            elif stack[0] == "}":
                if stack.pop() != "{":
                    return False
                else:
                    stack.pop(0)
                    closing += 1
            elif stack[0] == "]":
                if stack.pop() != "[":
                    return False
                else:
                    stack.pop(0)     
                    closing += 1
            index += 1   
        # We only need to go through string one more time is enough
        if len(stack) == 0 and closing == opening:
            return True
        else:
            return False
        