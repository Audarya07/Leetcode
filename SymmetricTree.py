# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.solver(root.left, root.right)

    def solver(self, left, right):
        if left == None or right == None:
            return left == right

        if left.val != right.val:
            return False

        return self.solver(left.left, right.right) and self.solver(left.right, right.left)
