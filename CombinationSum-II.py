# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.



# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # we sort the array so that duplicates can be compared side by side and ignored
        candidates.sort()       
        
        def backtrack(ans, curr, candidates, remain, start):
            if remain < 0:
                return 0
            elif remain == 0:
                ans.append(curr[:])
            else:
                for i in range(start, len(candidates)):
                    # if block to ignore duplicates
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    curr.append(candidates[i])
                    backtrack(ans, curr, candidates, remain-candidates[i], i+1)     # i+1 because each number in candidates may only be used once in the combination.
                    curr.pop()
        
        backtrack(ans, [], candidates, target, 0)
        return ans