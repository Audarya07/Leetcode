# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# "<<" to left shift by 1
# "|" to add next value
# Same as => "dec * 2 + head.next.val"
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        dec = head.val
        while head.next:
            dec = (dec << 1) | head.next.val
            head = head.next
        return dec