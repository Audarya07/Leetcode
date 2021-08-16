# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def robR(self, root):
        if not root:
            return (0, 0)
        left = self.robR(root.left)
        right = self.robR(root.right)
        
        curr_node = root.val + left[1] + right[1]
        not_curr_node = max(left) + max(right)
        return (curr_node, not_curr_node)
        
            
    def rob(self, root: Optional[TreeNode]) -> int:
        arr = self.robR(root)
        return max(arr)
    
# Solution
# 1. Manage a tuple [curr_node, not_curr_node]
#     where curr_node     --> rob current_node + rob grandchild_node
#           not_curr_node --> rob child_node
# 2. curr_node = ROB the node, then you can't rob the child/children of the node.
# 3. not_curr_node = SKIP the node, then you can ROB or SKIP the child/children of the node. 
   