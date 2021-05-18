# Given an integer array nums, in which exactly two elements appear only 
# once and all the other elements appear exactly twice. Find the two elements 
# that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity
 # and uses only constant extra space.

 

# Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.


# num:  00011001000
# rsbm: 00000001000

# separate the nums into 2 buckets based on rsb(right most set bit)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for val in nums:
            res ^= val
        
        #right most set bit mask(rsbm) helps us to differentiate 2 required nums
        rsbm = res & (-res)
        n1 = 0
        n2 = 0
        ans = []
        for val in nums:
            if val & rsbm == 0: 
                n1 ^= val
            else:
                n2 ^= val
        ans.append(n1)
        ans.append(n2)
        return ans