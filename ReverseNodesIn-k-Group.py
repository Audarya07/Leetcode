# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        prev = ans =  ListNode(None)
        cnt = 0 
        while head:
            head = head.next
            cnt += 1
        
        for _ in range(cnt//k):
            s = curr
            for i in range(k):
                node = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = node
            prev = s
        prev.next = curr
        return ans.next
