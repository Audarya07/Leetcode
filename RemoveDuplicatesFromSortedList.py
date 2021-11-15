# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp = ListNode(-1)
        temp.next = head
        prev = temp
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return temp.next
