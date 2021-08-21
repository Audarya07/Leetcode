# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        if not root:
            return []
        
        s = [(root, [root.val])]
        arr = []
        while s:
            node, x = s.pop()
            if not node.left and not node.right and sum(x) == target:
                arr.append(x)
            if node.left:
                s.append((node.left, x+[node.left.val]))
            if node.right:
                s.append((node.right, x+[node.right.val]))
        return arr
