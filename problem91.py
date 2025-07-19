class Solution:
    def numDecodings(self, s: str):
        # Decode secret message 
        # can have dictionry for each number in string
        # Or just make all possible numbers between 1 to 26
        # for each index possible number of time. 
        if len(s) == 1 and int(s[0]) > 0:
            return 1
        elif len(s) == 1 and int(s[0]) == 0:
            return 0
    
        if len(s) > 1 and int(s[0]) == 0:
            return 0
    
        # Save all possible combination of code in certain index
        dp = [0 for i in range(len(s))]
        dp[0] = 1
        for i in range(1, len(s)):
            if 0 != int(s[i]):
                dp[i] += dp[i-1]
                if 9 < int(s[i-1:i+1]) < 27:
                    if i == 1:
                        dp[i] = dp[i-1] + 1
                    elif i > 1:
                        dp[i] += dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if 0 < int(s[i-1]) < 3:
                    if i > 1:
                        dp[i] = dp[i-2]
                    else:
                        dp[i] = dp[i-1]
                else:
                    # This is case ...70..... -> there is no possible combination
                    return 0
        return dp[len(s)-1]