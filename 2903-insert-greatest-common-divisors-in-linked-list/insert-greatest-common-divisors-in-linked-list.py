# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)
        
        if not head.next:
            return head
        
        curr = head
        while curr.next:
            gcd_val = gcd(curr.val,curr.next.val)
            # Create a new node containing gcd value
            new_node = ListNode(gcd_val)
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            curr = temp
        
        return head