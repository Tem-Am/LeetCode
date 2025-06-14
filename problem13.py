############################
## Roman to Interger
############################
class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C" : 100, "D": 500, "M": 1000}
        i = 0
        ans = 0
        while i < len(s):
            if i < len(s)-1:
                if rom_dic[s[i]] < rom_dic[s[i+1]]:
                    ans = ans + rom_dic[s[i+1]] - rom_dic[s[i]]
                    i = i + 2
                else: 
                    ans = ans + rom_dic[s[i]]
                    i += 1
            else:
                ans += rom_dic[s[i]]
                i += 1
        return ans