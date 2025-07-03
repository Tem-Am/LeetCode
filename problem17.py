class Solution:
    def letterCombinations(self, digits: str):
        # Edge case: where size is 0, return empty list
        if len(digits) == 0:
            return []
        # It is all combination of each letters
        comb = []
        # Dictionary for number to string
        NumCon = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        # Create first letters for initialize
        for i in NumCon[digits[0]]:
            comb.append(i)
        if len(digits) == 1:
            return comb
        
        # D is single digit
        for d in range(1, len(digits)):
            # This array for next generated possible strings
            ans = []
            # C stands for each combination in comb list
            for c in comb:
                # l stands for single letter
                for l in NumCon[digits[d]]:
                    a = c + l
                    ans.append(a)
            comb = ans
        return comb
    
    # ChatGpt solution
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            for letter in digit_to_letters[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result
