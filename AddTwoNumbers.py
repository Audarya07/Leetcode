# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)  
# Output: 7 -> 0 -> 8  
# Explanation: 342 + 465 = 807.  


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode(0)
    curr = l3
    carry = 0
    p = l1
    q = l2

    while p or q:
        if p:
            x = p.val
        else:
            x = 0

        if q:
            y = q.val
        else:
            y = 0

        summ = x + y + carry
        carry = summ//10
        new_node = ListNode(summ%10)
        curr.next = new_node
        curr = curr.next

        if p:
            p = p.next
        if q:
            q = q.next

    if carry > 0:
            curr.next = ListNode(carry)
    return l3.next
