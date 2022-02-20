# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Example 1:

# Input: nums = [1,2,0]
# Output: 3

# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 1. Mark numbers (num < 0) and (num > n) with a special marker number (n+1) 
        # (we can ignore those because if all number are > n then we'll simply return 1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
                
        # all number in the array are now positive, in the range 1..n+1
        
        # 2. mark each cell appearing in the array, by changing the index for that number to negative
        for i in range(n):
            curr = abs(nums[i])
            if curr > n:
                continue
            
            curr -= 1   # -1 for zero index based array (so the number 1 will be at pos 0)
            
            if nums[curr] > 0:
                nums[curr] = -1 * nums[curr]
                
        # 3. find the first cell which isn't negative (doesn't appear in the array)
        for i in range(n):
            if nums[i] > 0:
                return i + 1
            
        # 4. no positive numbers were found, which means the array contains all numbers 1..n
        return n + 1
