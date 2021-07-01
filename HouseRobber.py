class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            if i % 2 ==0:
                a = max(nums[i]+a, b)
            else:
                b = max(nums[i]+b, a)
                
        return max(a, b)