class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        # Rcursive Solution
        def solver(root, ans):
            if root:
                if root.left:
                    solver(root.left,ans)
                ans.append(root.val)
                if root.right:
                    solver(root.right, ans)

        ans = []
        solver(root,ans)
        return ans

        # Iterative Solution
        ans = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans