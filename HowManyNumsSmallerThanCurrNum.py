class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dup = sorted(nums)
        ans = []
        for i in range(len(dup)):
            nums[i] = dup.index(nums[i])
        return nums