class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 0 XOR x = x
        # x XOR x = 0
        
        ans = 0
        for val in nums:
            ans = ans ^ val
        return ans
        