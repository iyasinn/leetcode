# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # L1 is the list we care about, l2 is the other
        carry = 0

        dummy = ListNode()
        tail = dummy


        while l1 or l2:

            val = carry

            if l1:
                val += l1.val
                l1 = l1.next
            if l2: 
                val += l2.val
                l2 = l2.next
            
            carry = 1 if val >= 10 else 0
            val = val % 10

            tail.next = ListNode(val)
            tail = tail.next
        
        if carry:
            tail.next = ListNode(1)

        
        return dummy.next
            
