# You are given a string s. You can convert s to a palindrome by 
# adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.

 
# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"

# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]
        new_s = s + "#" + rev_s
        
        lps = [0]*len(new_s)
    
        self.calc_lps(new_s, lps)
        print(lps)
        return rev_s[0: n-lps[-1]] + s

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
                    