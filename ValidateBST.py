# Input: root = [2,1,3]
# Output: true

# Input: root = [5,1,4,null,null,3,6]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solver(self, node, min_node, max_node):
        if not node:
            return True
        if (min_node and node.val <= min_node.val or max_node and node.val >= max_node.val):
            return False
        return self.solver(node.left, min_node, node) and self.solver(node.right, node, max_node)
        
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.solver(root, None, None)
    