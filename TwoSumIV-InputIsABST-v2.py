def dll(root):
    if not root:
        return None, None
    lh, lt = dll(root.left)
    rh, rt = dll(root.right)
    if lh:
        h = lh
        lt.right = root
        root.left = lt
    else:
        h = root
    if rh:
        t = rt
        root.right = rh
        rh.left = root
    else:
        t = root
    return h, t
    
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        h, t = dll(root)
        while h.val != t.val:
            summ = h.val + t.val
            if summ == k:
                return True
            if summ < k:
                h = h.right
            else:
                t = t.left
        return False