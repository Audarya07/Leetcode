class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solver(nums, start, end):
            if start == end:
                return nums[start]
            
            dp = [-1 for i in range(n)]

            dp[start] = nums[start]
            dp[start+1] = max(nums[start], nums[start+1])

            for i in range(start+2, end+1):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])

            return dp[end]
        
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        resOne = solver(nums, 0, n-2)
        resTwo = solver(nums, 1, n-1)
        
        return max(resOne, resTwo)
        