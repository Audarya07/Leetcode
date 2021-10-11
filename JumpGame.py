class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGoodIndex = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastGoodIndex:
                lastGoodIndex = i
        return lastGoodIndex == 0


# Solution 2
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if farthest < i:
                return False
            farthest = max(farthest, i + nums[i])
        
        return True
 