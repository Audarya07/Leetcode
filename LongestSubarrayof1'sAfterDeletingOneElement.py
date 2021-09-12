# Sliding Window
# TC = O(N)
# SC = O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        cnt = 0
        ans = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                cnt += 1
            while cnt > 1:
                if nums[i] == 0:
                    cnt -= 1
                i += 1
            ans = max(ans, j - i)
        return ans
        