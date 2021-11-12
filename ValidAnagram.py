# Ex1
# I/P => s = "anagram", t = "nagaram"
# O/P => true

# Ex2
# I/P => s = "rat", t = "car"
# O/P => false

# Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ctr = [0]*26
        for i in range(len(s)):
            ctr[ord(s[i]) - ord('a')] += 1;
            ctr[ord(t[i]) - ord('a')] -= 1;
        
        for i in range(26):
            if ctr[i] != 0:
                return False
        return True

# Solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cntr = Counter(s)
        if len(s) != len(t):
            return False
        
        for val in t:
            if val not in s_cntr:
                return False
            s_cntr[val] -= 1
        
        for val in s_cntr:
            if s_cntr[val] != 0:
                return False
        return True
