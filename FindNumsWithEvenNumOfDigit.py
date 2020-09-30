class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        
        for val in nums:
            if val == 100000:
                cnt += 1
            if (val > 9 and val < 100) or (val > 999 and val < 10000):
                cnt += 1
        return cnt