class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return helper(s, i+1, j) or helper(s, i, j-1)
            i += 1
            j -= 1
        return True