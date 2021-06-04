# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(ans, curr, nums):
            if len(curr) == len(nums):
                ans.append(curr[:])
            else:
                for i in range(len(nums)):
                    if nums[i] in curr:
                        continue
                    curr.append(nums[i])
                    backtrack(ans, curr, nums)
                    curr.pop()
        backtrack(ans, [], nums)
        return ans