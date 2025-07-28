class Solution:
    def groupAnagrams(self, strs: List[str]):
        # Base cases:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [[strs[0]]]

        # go through everything 
        # checking and adding in set or dictionary;
        # we can sort them in and check in dictionary and add index if it exists there

        anagrams = {} # hash table for words
        for i in range(len(strs)):
            sorted_str = sorted(strs[i])
            newStr = "".join(sorted_str)
            if newStr in anagrams:
                anagrams[newStr].append(strs[i])
            else:
                anagrams[newStr] = [strs[i]]
        ans = []
        for value in anagrams.values():
            ans.append(value)
        return ans