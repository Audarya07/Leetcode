# You are given a sorted array consisting of only integers where every 
# element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        
        # Boundary checks
        if h == 0:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[h] != nums[h-1]:
            return nums[h]
        
        # binary search
        while l <= h:
            m = (l+h)//2
            
            # unique element found
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]

            # index of pair[0] should be even and pair[1] be odd 
            if (m%2==0 and nums[m] == nums[m+1]) or (m%2 != 0 and nums[m] == nums[m-1]):
                l = m + 1

            else:
                h = m -1
        
        return -1
