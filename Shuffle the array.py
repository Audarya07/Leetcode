class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = len(nums) // 2
        ans = []
        while i <=j and j < len(nums):
            ans.append(nums[i])
            i += 1
            ans.append(nums[j])
            j += 1
        return ans