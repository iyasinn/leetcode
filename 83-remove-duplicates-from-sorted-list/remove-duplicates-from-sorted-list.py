# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# We have to go thru th elinked list 
# For each node
# Comapare the first node to every forward node UNTIL you see the next highest value, so not the same value 
# And then mkae the first node connect to the second

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pointer = head 

        # Run the algorithm on EVERY node
        while pointer != None: 
            second = pointer.next 

            # remove the duplicates, or skip the duplicates
            while second != None and second.val == pointer.val:
                second = second.next

            pointer.next = second
            pointer = pointer.next
        
        return head 




        