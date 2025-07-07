class Solution:
    def intToRoman(self, num: int):
        int_dic = {1000 : "M", 900 : "CM", 500 : "D",
                    400: "CD", 100: "C", 90: "XC", 50: "L",
                    40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        # In general, XYZT is given number,
        # Then, we need to make X000 first, Y00 second, then go on.
        ans = []
        for i in int_dic:
            while num >= i:
                ans.append(int_dic[i])
                num -= i
        number = "".join(ans)
        return number             
