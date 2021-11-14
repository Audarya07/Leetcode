# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1 -> DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        if left > right:
            return left + 1
        else:
            return right + 1


# Solution 2 --> BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = [root]
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                left = q[0].left
                if left:
                    q.append(left)
                
                right = q[0].right
                if right:
                    q.append(right)
                
                q.pop(0)
        return depth
