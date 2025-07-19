def longestConsecutive(nums):
        # Base cases where no need to do any calculation
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        # Set that has key which can be all uniqe number 
        seq = set()   
        for num in nums:
            seq.add(num)
        
        # Includes all the sequence length here
        sequences = []
        
        # Set has all the number from list without any duplicates
        for number in seq:
            # if there is no number less in seq
            # It means that number is starting point
            if number-1 not in seq:
                sequence = 1
                number += 1
                while number in seq:
                    sequence += 1   
                    number += 1
                sequences.append(sequence)
        longest = 0
        for l in sequences:
            if l > longest:
                longest = l
        return longest

print(
    longestConsecutive([100,4,200,1,3,2]),
    longestConsecutive([0,3,7,2,5,8,4,6,0,1]),
    longestConsecutive([1,0,1,2]),
    longestConsecutive([0,0,]),
    longestConsecutive([1])
)

