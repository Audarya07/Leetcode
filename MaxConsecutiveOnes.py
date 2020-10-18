#Can be solved using 2 pointer approach also

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxx = 0
        for val in nums:
            if val == 1:
                cnt += 1
                maxx = max(maxx, cnt)
            else:
                cnt = 0
        return maxx