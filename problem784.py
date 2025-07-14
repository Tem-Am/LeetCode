class Solution:
    def letterCasePermutation(self, s: str):
        # loop through all string
        # each string can be one written two ways
        digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        comb = []
        # Make all lower case/ same as sorting them
        lowerCase = s.lower()

        def zeros(l : List[str], newIndex):
            newComb = []
            for letter in l:
                lower = letter[:newIndex] + letter[newIndex] + letter[newIndex+1:]
                upper = letter[:newIndex] + letter[newIndex].upper() + letter[newIndex+1:]
                newComb.append(lower)
                newComb.append(upper)
            print(newComb)
            return newComb
        init = [lowerCase]
        for i in range(len(s)):
            if s[i] not in digit:
                temp = zeros(init, i)
                init = temp
        return init

