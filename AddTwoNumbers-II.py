# Example 1:
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]

# Example 2:
# Input: l1 = [1], l2 = [9,9]
# Output: [1,0,0]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1 : By reversing th LL
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            prev = None
            curr = head
            cnt = 0
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                cnt += 1
            return prev
        
        rev_l1 = reverse(l1)
        rev_l2 = reverse(l2)

        l3 = ListNode(0)
        curr = l3
        carry = 0
        p = rev_l1
        q = rev_l2

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
        return reverse(l3.next)


# Solution 2: By using stack (better solution)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 , stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        head = None
        
        while stack1 or stack2 or carry:
            val1, val2 = 0, 0
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            
            summ = val1 + val2 + carry
            digit = summ % 10
            carry = summ // 10
            new_head = ListNode(digit)
            new_head.next = head
            head = new_head
        return head