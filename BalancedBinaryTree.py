# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# TC - O(N)

def height(node):
    if not node:
        return 0
    
    lh = height(node.left)
    if lh == -1:
        return -1
    
    rh = height(node.right)
    if rh == -1:
        return -1
    
    if abs(lh - rh) > 1:
        return -1
    
    return max(lh, rh) + 1

        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:   
        return height(root) != -1        
        
##############################################################

# TC - O(N^2)
def height(node):
    if not node:
        return 0
    return max(height(node.left), height(node.right)) + 1

        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:   
        if not root:
            return True
        
        left_h = height(root.left)
        right_h = height(root.right)
        
        if abs(left_h - right_h) > 1:
            return False
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        
        if not left or not right:
            return False
        
        return True
        
        
        
        