# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
#              2 is the missing number in the range since it does not appear in nums.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XORing the numbers twice:
        #   1. with array value itself
        #   2. with index (these are expected values in the array)
        # will eliminate the existing numbers except for the missing number
        
        n = len(nums)
        for i in range(n):
            n ^= nums[i]
            n ^= i
        return n