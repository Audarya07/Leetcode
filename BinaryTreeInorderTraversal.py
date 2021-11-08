# Solution 1 --> Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
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

# Solution 2 --> Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        return ans


# Iterative approach:
# - If node not null --> put in stack and move LEFT
# - Else
#     - if stack is empty --> traversal done.. so break
#     - else remove top element of the stack and append in the ans array, then move RIGHT
