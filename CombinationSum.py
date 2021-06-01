# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers 
# sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers
# is different.



# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(ans, curr, candidates, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                ans.append(curr[:])
            else:
                for i in range(start, len(candidates)):
                    curr.append(candidates[i])
                    backtrack(ans, curr, candidates, remain-candidates[i], i)
                    curr.pop()
        
        backtrack(ans, [], candidates, target, 0)
        return ans