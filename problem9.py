class Solution:
    def isPalindrome(self, x: int):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False