class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ans = 0
        left_mx = curr_mx = nums[0]
        for i in range(len(nums)):
            curr_mx = max(curr_mx, nums[i])
            if nums[i] < left_mx:
                left_mx = curr_mx
                ans = i
        return ans + 1
                