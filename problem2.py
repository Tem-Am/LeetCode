#######################################################################
## Adding two number and return value in single linked list reversed order
#######################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = 0
        number2 = 0
        # Since linked list is reverse order, we multiple next number by 10 and add to main number
        ten1 = 1
        ten2 = 1
        # loop through l1 linked list
        while l1 != None:
            # Add each value to number 
            number1 += l1.val * ten1
            ten1 *= 10
            l1 = l1.next
        while l2 != None:
            number2 += l2.val * ten2
            ten2 *= 10
            l2 = l2.next
        result = number1 + number2
        listOfValue = []
        if result == 0:
            listOfValue.append(0)
        while result > 0:
           listOfValue.append(result % 10)
           result = result // 10
        # First node of result 
        head = ListNode(listOfValue[0])
        current = head
        for val in listOfValue[1:]:
            current.next = ListNode(val)
            current = current.next
        return head