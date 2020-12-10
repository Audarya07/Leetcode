#Given an array of size n, find the majority element.
#The majority element is the element that appears more than ⌊ n/2 ⌋ times.

#SOLUTION : Using Boyer-Moore Voting Algorithm
#1) Initil element is candidate maximimum occuring value (curr)
#2) If next val is same as candidate, incr cnt
#3) Else, decr cnt
#4) If cnt becomes zero, initialize the next value as candidate

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        curr = None
        for val in nums:
            if cnt == 0:
                curr = val
            if val == curr:
                cnt += 1
            else:
                cnt -= 1
        return curr

# TC: O(N)
# SC: O(1)