class Solution:
    def simplifyPath(self, path: str):
        parts = path.split("/") # split by /
        stack = []
        for p in parts:
            if p == '..':
                if len(stack) != 0:
                    stack.pop()
            elif p != '.' and p != '':
                stack.append(p)
        
        if len(stack) == 0:
            return "/"
        newpath = ""
        for s in stack:
            newpath += "/" + s
        return newpath