#             1
#           /   \
#          3     2
#        /   \    \  
#       [5]   3   [9] 

# Output: 4     -> index of 9 minus index of 5 
#----------------------------
#            1
#          /   \
#         3     2
#          \     \  
#          [3]   [9] 

# Output: 3     -> index of 9 minus index of 3 


def getwidth(root, rootlevel, rootindex, widthmap):
    if root:
        if rootlevel not in widthmap:
            widthmap[rootlevel] = [rootindex, rootindex]
        elif rootindex < widthmap[rootlevel][0]:
            widthmap[rootlevel][0] = rootindex
        elif rootindex > widthmap[rootlevel][1]:
            widthmap[rootlevel][1] = rootindex
        getwidth(root.left, rootlevel+1, 2*rootindex+1, widthmap)
        getwidth(root.right, rootlevel+1, 2*rootindex+2, widthmap)
            
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        widthmap = {}
        getwidth(root, 0, 0, widthmap)
        return max([1+level[1]-level[0] for level in widthmap.values()])       
