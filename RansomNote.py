class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        b = Counter(magazine)
        for val in ransomNote:
            if val not in b:
                return False
            
            b[val] -= 1
            if b[val] < 0:
                return False
        return True
