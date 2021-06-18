class Solution:
    def maxDepth(self, s: str) -> int:
        depth = float('-inf')
        left = 0
        right = 0
        for x in s:
            if x == "(":
                left += 1
            elif x == ")":
                right += 1
            depth = max(depth, left - right)
        return depth
                