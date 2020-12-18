class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastFound = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastFound], nums[i] = nums[i], nums[lastFound]
                lastFound += 1

# TC : O(N)
# SC : O(1)