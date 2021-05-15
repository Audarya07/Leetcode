# Input:
#              20
#             /   \
#            8     22
#           / \
#          4   12
#             /  \
#            10   14

# K(data of x) = 8
# Output: 10
# Explanation:
# Inorder traversal: 4 8 10 12 14 20 22
# Hence, successor of 8 is 10.

class Solution:
    def inorderSuccessor(self, root, x):
        if root.data == x.data:
            curr = root.right
            if not curr:
                return curr
            while curr.left:
                curr = curr.left
            return curr
        if root.data > x.data:
            ans = self.inorderSuccessor(root.left, x)
            return ans if ans else root
        return self.inorderSuccessor(root.right, x)
