# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy variable
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        # Traverse the LL and look for duplicate
        while curr:
            if curr.next and curr.val == curr.next.val:
                # Continue if there is duplicate
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                # If there are no duplicates, update prev
                prev = prev.next
            curr = curr.next
        
        return dummy.next