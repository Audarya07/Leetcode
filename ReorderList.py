# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        start_head = head
    
        n = len(stack)
        size = n//2 if n%2 == 0 else n//2+1
        while len(stack) > size:
            end_node = stack.pop()    
            nxt_node = start_head.next
            
            end_node.next = None
            start_head.next = end_node
            end_node.next = nxt_node
            start_head = nxt_node
        
        if start_head:
            start_head.next = None