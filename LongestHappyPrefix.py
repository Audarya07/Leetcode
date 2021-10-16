class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0]*len(s)
        n = len(s)
        lps[0] = 0
        j = 0
        i = 1
        while i < n:
            if s[i] == s[j]:
                lps[i] = j + 1
                j += 1
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[j] = 0
                    i += 1
        return s[:j]
