# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)
        
        dummy = ListNode(None)
        curr = dummy
        while heap:
            val = heapq.heappop(heap)
            curr.next = val
            curr = curr.next
            if val.next:
                heapq.heappush(heap, val.next)
        return dummy.next
