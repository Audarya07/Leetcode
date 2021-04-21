class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left:
            if not root.right:  #not left and not right means leaf node
                return 1
            return 1 + self.minDepth(root.right)    #not left only right then move right
        
        if not root.right:      #only left not right so move left
            return 1 + self.minDepth(root.left)
        
        #both left and right so min of both 
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) 