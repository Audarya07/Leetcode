# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # find middle node of LL
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse 2nd half of the LL
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        # compare head(1st half) and reversed half
        while node:
            if head.val != node.val:
                return False
            node = node.next
            head = head.next
        
        return True