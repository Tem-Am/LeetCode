class Solution:
    def plusOne(self, digits: List[int]):
        if len(digits) == 1:
            if digits[0] == 9:
                return [1,0]
            else:
                return [digits[0]+1]
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # this means that it is over len of digit
        digits.insert(0, 1)
        return digits