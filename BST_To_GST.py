# Given the root of a Binary Search Tree (BST), 
# convert it to a Greater Tree such that every key 
# of the original BST is changed to the original key 
# plus sum of all keys greater than the original key in BST.

def gst(root, summ):
    if not root:
        return summ
    summ = gst(root.right, summ)
    root.val += summ
    summ = root.val
    return gst(root.left, summ)
    
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        gst(root, 0)
        return root