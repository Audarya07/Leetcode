# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6


# Kadanes Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = final_max = nums[0]
        for num in nums[1:]:
            curr_max = max(num, curr_max+num)
            final_max = max(final_max, curr_max)
        return final_max