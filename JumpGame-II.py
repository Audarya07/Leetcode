class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy Solution : TC -> O(N)
        n = len(nums)
        left = right = 0
        res = 0
        farthest = 0

        for i in range(n-1):
            farthest = max(farthest, i+nums[i])

            if i == right:
                res += 1
                right = farthest

        return res

        # DP Solution: TC -> O(N^2)
#         n = len(nums)
#         dp = [ float('inf') for _ in range(n)]
#         dp[0] = 0

#         for i in range(1, n):
#             for j in range(i):
#                 if j+nums[j] >= i:
#                     dp[i] = min(dp[i], dp[j]+1)
#         return dp[n-1] 
