# Ex1
# I/P => s = "anagram", t = "nagaram"
# O/P => true

# Ex2
# I/P => s = "rat", t = "car"
# O/P => false


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