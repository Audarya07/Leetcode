class Solution:
    def maxPower(self, s: str) -> int:

        #2 Pointer solution
        n = len(s)
        if n == 1:
            return 1
        cnt = 0
        maxx = 0
        i = 0
        j = 0
        while j < n:
            if s[i] == s[j]:
                cnt += 1
            else:
                i = j
                cnt = 1
            j += 1
            maxx = max(cnt, maxx)
        return maxx