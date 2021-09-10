# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # post   =   left -> right -> root
        # inorder=   left -> root -> right
        m_dict = {}
        for idx, val in enumerate(inorder):
            m_dict[val] = idx

        # Note: in postorder root is the last element
        pidx = len(postorder) - 1
        
        def construct(start, end, post, pidx, m_dict):
            if start > end:
                return None, pidx
            root = TreeNode(post[pidx])
            
            pidx -= 1
            idx = m_dict[root.val]
            
            # Note: first construct right tree then left tree as below
            # if sequence changed --> doesn't work
            root.right, pidx = construct(idx+1, end, post, pidx, m_dict)
            root.left, pidx = construct(start, idx-1, post, pidx, m_dict)
            
            return root, pidx
            
        return construct(0, len(postorder)-1, postorder, pidx, m_dict)[0]
        