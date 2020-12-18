class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        unique = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in unique:
                ans.append(i)
        return ans