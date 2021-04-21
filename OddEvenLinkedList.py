# Input: head = [2,1,3,5,6,4,7]
# Output:       [2,3,6,7,1,5,4]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        odd = head
        even = head.next
        while odd.next and even.next:
            ncurr = odd.next
            odd.next = ncurr.next
            odd = odd.next
            ncurr.next = odd.next
            
        odd.next = even
        return head
        
# TC = O(N)
# SC = O(1)