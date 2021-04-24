def sameTreeStructure(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t1.val == t2.val and \
    	sameTreeStructure(t1.left,t2.left) and \
    	sameTreeStructure(t1.right, t2.right)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return s != None and \
        		(sameTreeStructure(s, t) or	\
        		self.isSubtree(s.left, t) or \
        		self.isSubtree(s.right, t))