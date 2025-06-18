class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if not strs:
            return ""
        
        # Flag for all letters are same for each strings
        output = ""
        index = 0
        # Loop until checking is true
        while True:
            # Compare each index from each strings with first strings
            # It does not matter with compare with which string since they all need to be same
            for i in range(len(strs)):
                # If one of them string's length is less than index, we will return that output
                if len(strs[i])-1 < index or strs[i][index] != strs[0][index]:
                    return output
            output += strs[0][index]
            index += 1
