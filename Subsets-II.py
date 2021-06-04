class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Solution 1
        # temp = [[]]
        # ans = []
        # for val in nums:
        #     temp += [[val]+x for x in temp]
        
        # for curr in temp:
        #     if sorted(curr) not in ans:
        #         ans.append(sorted(curr))
        # return ans
        
        
        # Solution 2
        ans = []
        nums.sort()
        
        def backtrack(ans, curr, nums, start):
            ans.append(curr[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(ans, curr, nums, i+1)
                curr.pop()
        
        backtrack(ans, [], nums, 0)
        return ans
        