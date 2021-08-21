# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution
class Solution:
    def hasPathSum(self, root: TreeNode, x: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right and x-root.val == 0:
            return True
        left = self.hasPathSum(root.left, x-root.val) 
        right = self.hasPathSum(root.right, x-root.val)
        
        return left or right


# Iterative solution
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        
        s = [(root, root.val)]
        while s:
            node, x = s.pop()
            if not node.left and not node.right and x == target:
                return True
            if node.left:
                s.append((node.left, node.left.val + x))
            if node.right:
                s.append((node.right, node.right.val + x))
        return False
