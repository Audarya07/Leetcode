# lp = left longest path
# rp = right longest path
# lw = left width
# rw = right width

# solver(root)[0] returns longest path
# solver(root)[1] returns largest width i.e diameter
# ----------------------------------------------------------------------


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def solver(node):
    if node is None:
        return 0, 0
    lp, lw = solver(node.left)
    rp, rw = solver(node.right)
    return max(lp, rp)+1, max(lw, rw, 1+lp+rp)  # +1 in 2nd return value for including root node

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return solver(root)[1] - 1
        