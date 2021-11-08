# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1 --> Recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def solver(arr, root):
            if root:
                arr.append(root.val)
                solver(arr, root.left)
                solver(arr, root.right)
                
        solver(arr, root)
        return arr

# Solution 2 --> Iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            # Add curr.right to stack first since the stack is FILO
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res
