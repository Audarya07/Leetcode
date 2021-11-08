# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def solver(root, ans):
            if root:
                if root.left:
                    solver(root.left, ans)
                if root.right:
                    solver(root.right, ans)
                ans.append(root.val)

        solver(root,ans)
        return ans
