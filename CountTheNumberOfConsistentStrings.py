class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        m = [0]*26
        res = len(words)
        for x in allowed:
            m[ord(x)-97] += 1
            
        for word in words:
            for ch in word:
                if m[ord(ch)-97] == 0:
                    res -= 1
                    break
        return res