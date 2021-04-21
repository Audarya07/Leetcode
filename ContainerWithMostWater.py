# Input: height = [4,3,2,1,4]
# Output: 16

class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        max_water = 0
        
        while l < r:
            curr_water = min(h[l], h[r]) * (r-l)
            max_water = max(max_water, curr_water)
            
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1

        return max_water
            