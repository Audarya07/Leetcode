class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == target:
                    return summ
                if abs(summ - target) < abs(res - target):
                    res = summ
                if summ > target:
                    k -= 1
                else:
                     j += 1
        return res