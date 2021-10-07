# Bottom Up
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [-1 for i in range(n)]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[n-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            if i % 2 ==0:
                a = max(nums[i]+a, b)
            else:
                b = max(nums[i]+b, a)
                
        return max(a, b)


# Recursive + Memo (top down)
class Solution:
    def robR(self, nums, dp, x):
        if x < 0:
            return 0
        if dp[x] >= 0:
            return dp[x]
        ans = max(nums[x]+self.robR(nums, dp, x-2), self.robR(nums, dp, x-1))
        dp[x] = ans
        return ans
    
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]
        return self.robR(nums, dp, len(nums)-1)
