# Solution using KMP pattern search algorithm

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        flag = 0
        n = len(haystack)
        m = len(needle)
        
        if not m:
            return 0
        
        lps = [0]*m
        self.calc_lps(needle, lps)
        
        i = 0
        j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            if j == m:
                flag = 1
                return i-j      #needle found
        if flag == 0:
            return -1
    
    def calc_lps(self, pat, lps):
        m = len(pat)
        l = 0
        i = 1
        lps[0] = 0
        while i < m:
            if pat[i] == pat[l]:
                lps[i] = l+1
                l += 1
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
                    