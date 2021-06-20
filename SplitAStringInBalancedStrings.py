class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        ans = 0 
        for x in s:
            if x == "L":
                cnt += 1
            elif x == "R":
                cnt -= 1
            if cnt == 0:
                ans += 1
        return ans 
            