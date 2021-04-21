# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right) 
            if len(level) > 0:
                # print(level)
                ans.append(level)
        return ans