####################
# Find the longest Palidromic Substring
####################

## My solution
def longestPalindrome(self, s: str) -> str:
    # Pc stands for possible combination from s 
        pc = len(s)
        answer = ''
        # Since we are going from the top to bottom, once we found the  word, it should be the longest
        while pc > 0:
            # Temp is for getting pc number
            temp = pc
            index = 0
            while temp <= len(s):
                # We will check every possible words given pc index 
                newWord = s[index:temp]
                if newWord == newWord[::-1]:
                    answer = newWord
                    # When we find it, we will stop it
                    return answer
                index += 1
                temp += 1
            pc -= 1
        return answer

## More efficient solution
def longestPalindrome(self, s: str) -> str:
        # When length is less 2, we will return s
        if len(s) < 2:
            return s
        
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expand_from_center(s, i, i)       # Odd length
            len2 = self.expand_from_center(s, i, i + 1)   # Even length
            max_len = max(len1, len2)
            
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

def expand_from_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # actual palindrome length