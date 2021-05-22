# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    val = [nums[i], nums[l], nums[r]]
                    res.append(val)
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res