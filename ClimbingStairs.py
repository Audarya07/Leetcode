class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        
        if n <= 1:
            return 1
        
        dp[0] = 1   # num of ways if 0 stairs = 1 (dont't climb)
        dp[1] = 1   # num of ways if 1 stair = 1 (take 1 step)
        dp[2] = 2   # num of ways if 2 stairs = 2 (take 1 step or 2 steps)
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
