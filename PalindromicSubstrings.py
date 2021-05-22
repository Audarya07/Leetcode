# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[0 for j in range(n)] for i in range(n)]
        
        # diagonal will have all single chars i.e palindromes
        # input = abcd --> a  b  c  d are
        for i in range(n):
            dp[i][i] = 1
            count += 1
        
        for i in range(n-1):       
            if(s[i] == s[i+1]):
                dp[i][i+1] = 1
                count += 1
        
        for j in range(2, n):
            for i in range(n-1):
                if(s[i] == s[j] and dp[i+1][j-1]):
                    dp[i][j] = 1
                    count += 1
        
        return count
