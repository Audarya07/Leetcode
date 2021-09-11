# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1



# Sliding Window
# TC = O(N)
# SC = O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        summ = 0
        ans = float('inf')
        
        for j in range(len(nums)):
            summ += nums[j]
            while summ >= target:
                ans = min(ans, j-i+1)       # (j-i+1) is the window size
                summ -= nums[i]
                i += 1    

        if ans == float('inf'):
            return 0
        return ans
        