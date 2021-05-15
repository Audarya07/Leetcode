# Solution 2

class Solution:
    def find(self, root, key):
        if not root:
            return None
        elif root.data == key.data:
            return root
        elif root.data < key.data:
            return self.find(root.right, key)
        else:
            return self.find(root.left, key)
    
    def findMin(self,root):
        if not root:
            return None
        while root.left != None:
		    root = root.left;
	    return root
    
    def inorderSuccessor(self, root, x):
        curr = self.find(root, x)
        if not curr:
            return None
        if curr.right != None:
            return self.findMin(curr.right)
        else:
            succ = None
            ance = root
            while ance != curr:
                if curr.data < ance.data:
                    succ = ance
                    ance = ance.left
                else:
                    ance = ance.right
            return succ