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
