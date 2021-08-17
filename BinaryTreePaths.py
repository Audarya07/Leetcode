# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        s = [(root, "")]
        arr = []
        while s:
            node, path = s.pop()
            if not node.left and not node.right:
                arr.append(path+str(node.val))
            if node.right:
                s.append((node.right, path+str(node.val)+"->"))
            if node.left:
                s.append((node.left, path+str(node.val)+"->"))
        return arr
