class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # First uses s.split to split each words into list
        listOfWord = s.split()
        # Then create dictionaries for each letters and words to mapping
        word_dic = {}
        letter_dic = {}
        
        # Return false if len of s and pattern are not equal
        if len(pattern) != len(listOfWord):
            return False

        # Loop through each letter and words
        for i in range(len(pattern)):
            # Check if next word or letter exist in each dictionry 
            # If they are exist, we see value of letter_dic is same this word
            # and value of word_dic is same as this letter
            if listOfWord[i] in word_dic and pattern[i] in letter_dic:
                # Check if letter also exist in dic
                if listOfWord[i] != letter_dic[pattern[i]] or pattern[i] != word_dic[listOfWord[i]]:
                    return False   
        # If different words have same value, we also return false.   
            elif listOfWord[i] in word_dic or pattern[i] in letter_dic:
                return False
            else:
                word_dic[listOfWord[i]] = pattern[i]
                letter_dic[pattern[i]] = listOfWord[i]
            
        return True