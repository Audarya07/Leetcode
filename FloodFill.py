# You are also given three integers sr, sc, and newColor. 
# You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, 
# plus any pixels connected 4-directionally to the starting pixel of the same color 
# as the starting pixel, plus any pixels connected 4-directionally to those pixels 
# (also with the same color), and so on. Replace the color of all of the 
# aforementioned pixels with newColor.

class Solution:
    def floodFill(self, nums: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if nums[sr][sc] ==newColor:
            return nums
        
        self.dfs(nums, sr, sc, nums[sr][sc], newColor)
        return nums
    
    def dfs(self, nums, x, y, color, newColor):
        if x < 0 or y < 0 or x >= len(nums) or y >= len(nums[0]) or nums[x][y] != color:
            return
        
        nums[x][y] = newColor
        self.dfs(nums, x+1, y, color, newColor)
        self.dfs(nums, x, y+1, color, newColor)        
        self.dfs(nums, x-1, y, color, newColor)        
        self.dfs(nums, x, y-1, color, newColor)        