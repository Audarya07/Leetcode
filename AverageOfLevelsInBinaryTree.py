# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        if not root:
            return ans
        
        q = [root]
        
        while q:
            summ = 0
            cnt = 0
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                summ += node.val
                cnt += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            a = summ/cnt
            ans.append(round(a,5))
        return ans
    