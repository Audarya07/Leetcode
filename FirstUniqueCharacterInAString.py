class Solution:
    def firstUniqChar(self, s: str) -> int:
        cntr = {}
        for i in range(len(s)):
            if s[i] in cntr:
                cntr[s[i]] += 1
            else:
                cntr[s[i]] = 1
        
        for i in range(len(s)):
            if cntr[s[i]] == 1:
                return i
        return -1
