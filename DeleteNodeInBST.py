class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        #key < root value, so search key in left subtree
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        #key > root value, so search key in right subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        #key == root value
        else:
            #if right subtree not exist, return left subtree to parent
            if not root.right:
                return root.left
            #if right subtree exist, find min node in left part of the right subtree
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left
                #replace root value with min value found above
                root.val = temp.val
                #delete the min value node(temp) from its location i.e right subtree
                root.right = self.deleteNode(root.right, temp.val)
        return root