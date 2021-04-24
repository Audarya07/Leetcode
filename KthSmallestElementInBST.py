#Given the root of a binary search tree, and an integer k, 
#return the kth (1-indexed) smallest element in the tree.


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#---------------------------------------
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


def helper(root, ans):
    if root:
        if root.left:
            helper(root.left, ans)
        ans.append(root.val)
        if root.right:
            helper(root.right, ans)
        
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        helper(root, ans)
        return ans[k-1]