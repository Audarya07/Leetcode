class Solution:
    def numberOfSteps (self, num: int) -> int:
        if not num:
            return 0
        cnt = 0
        while num:
            if num & 1:  #if num&1 != 0,means num is odd,so we reduce by 1 then divide
                cnt += 2
            else:
                cnt += 1
            num >>= 1
        return cnt - 1