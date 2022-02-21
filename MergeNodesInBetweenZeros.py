# Example 1
# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 3 + 1 = 4.
# - The sum of the nodes marked in red: 4 + 5 + 2 = 11.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero = head
        curr = head.next
        
        while curr:
            if curr.val != 0:
                zero.val += curr.val
            else:
                if curr.next == None:
                    zero.next = None
                else:
                    zero.next = curr
                zero = curr
            curr = curr.next
            
        return head
