# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

#start with root node i.e 1st item in preorder sequence.
#find boundary of its left and right subtree in inorder seq.
#all keys before root in inorder becomes left subtree.
#all keys after root in inorder becomes right subtree.
#repeat this recursively for all nodes.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(start, end, preorder, preIndex, nmap):
    if start > end:
        return None, preIndex
    
    # The next element in preorder will be the root node of subtree
    # formed by sequence represented by inorder[start, end]
    root = TreeNode(preorder[preIndex])
    preIndex += 1
    
    # get the index of the root node in inorder to determine the
    # left and right subtree boundary
    index = nmap[root.val]
    
    # recursively construct the left subtree
    root.left, preIndex = helper(start, index-1, preorder, preIndex, nmap)

    # recursively construct the right subtree
    root.right, preIndex = helper(index+1, end, preorder, preIndex, nmap)
    
    return root, preIndex

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        #preIndex stores the index of the next unprocessed node in a preorder sequence
        #start with the root node(present at 0th index)
        preIndex = 0
        
        #dict to find index of any element in given inorder sequence
        nmap = {}
        for i, v in enumerate(inorder):
            nmap[v] = i

        return helper(0, len(inorder)-1, preorder, preIndex, nmap)[0]