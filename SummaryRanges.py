class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        res = []
        while i < n:
            val = nums[i]
            while i < n-1 and nums[i+1] -nums[i] == 1:
                i += 1
            if val != nums[i]:
                res.append(str(val)+"->"+str(nums[i]))
            else:
                res.append(str(nums[i]))
            
            i += 1
        return res
        