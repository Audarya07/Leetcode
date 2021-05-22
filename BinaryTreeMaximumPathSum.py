# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxx = [float('-inf')]
        
        def solver(node, res):
            if not node:
                return 0
            left = solver(node.left, res)
            right = solver(node.right, res)
            temp = max(max(left, right) + node.val, node.val)
            ans = max(temp, left+right+node.val)
            res[0] = max(res[0], ans)
            return temp

        solver(root, maxx)
        return maxx [0]