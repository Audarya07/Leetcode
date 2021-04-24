# Given the root node of a binary search tree, 
# return the sum of values of all nodes with a value in the range [low, high].


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32


def inorder(root, ans):
    if root:
        inorder(root.left, ans)
        ans.append(root.val)
        inorder(root.right, ans)
        
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = []
        inorder(root, ans)      #'ans' contains sorted values of tree nodes [3, 5, 7, 10, 15, 18]
        summ = 0
        for i in range(len(ans)):
            if ans[i] >= low and ans[i] <= high:
                summ += ans[i]
        return summ