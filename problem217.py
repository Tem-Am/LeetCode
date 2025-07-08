class Solution:
    def containsDuplicate(self, nums: List[int]):
        # Need to save it from the list with uniq element
        uniqList = set()
        for i in nums:
            if i in uniqList:
                return True
            uniqList.add(i)
        return False