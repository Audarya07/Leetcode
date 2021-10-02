class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for i in range(n)]
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
        return min(dp[n-1], dp[n-2])
        # there are 2 ways to reach top:
        #   1. from prev step dp[i-1] 
        #   2. from prev prev step dp[i-2]
        
