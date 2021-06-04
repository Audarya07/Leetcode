class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution 1
        # ans = [[]]
        # for val in nums:
        #     ans += [[val] + x for x in ans]
        # return ans
        
        
        # Solution 2
        ans = []
        nums.sort()
        
        def backtrack(ans, curr, nums, start):
            ans.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(ans, curr, nums, i+1)
                curr.pop()
        
        backtrack(ans, [], nums, 0)
        return ans
        
        
                