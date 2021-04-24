def findNode(root, k, nset):
    if not root:
        return False
    if k-root.val in nset:
        return True
    nset.add(root.val)
    
    return findNode(root.left, k, nset) or findNode(root.right, k, nset);
    
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nset = set()
        return findNode(root, k, nset)