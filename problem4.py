class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        # Index of two arrays
        index1 = 0
        index2 = 0
        totalNum = len(nums1) + len(nums2)
        newArray = []
        # Loop until all items into to newArray
        while len(newArray) < totalNum:
            # All numbers from nums1 in newArray, add remaining numbers from nums2
            if index1 == len(nums1) :
                newArray.append(nums2[index2])
                index2 += 1
            # All numbers from nums2 in newArray, add remaining numbers from nums1
            elif index2 == len(nums2):
                newArray.append(nums1[index1])  
                index1 += 1
            elif nums1[index1] < nums2[index2]:
                newArray.append(nums1[index1])
                index1 +=1
            else:
                newArray.append(nums2[index2])
                index2 += 1
                
        # Find the median and check if total number is even or odd.
        medIndex = len(newArray) // 2
        if len(newArray) % 2 == 0:
            return (newArray[medIndex-1] + newArray[medIndex])/2
        else:
            return newArray[medIndex]
