class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        summ = 0
        for val in nums:
            summ += val
            ans.append(summ)
        return ans