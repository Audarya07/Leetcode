
# Recursive Top Down Approach
# TC: O(N logN) + O(N)  --> sorting + DP
class Solution:
    def recur(self, nums, dp, idx):
        if idx == len(nums):
            return 0
        
        if dp[idx] == -1:
            earn = nums[idx]
            skip = idx + 1
            
            while skip < len(nums) and nums[skip] == nums[idx]:
                earn += nums[skip]
                skip += 1
        
            while skip < len(nums) and nums[skip] == nums[idx] + 1:
                    skip += 1

            earn += self.recur(nums, dp, skip)

            ignore = self.recur(nums, dp, idx + 1)
        
            dp[idx] = max(earn, ignore)
        
        return dp[idx]

    
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        dp = [-1 for i in range(len(nums))]
        return self.recur(nums, dp, 0)
