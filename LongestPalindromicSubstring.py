class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]
        maxLen = 1
        start = 0

        #all single letter are palindromes
        for i in range(n):
            dp[i][i] = 1
        
        #check for size 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                maxLen = 2
                start = i
                
        #check for size >= 3
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k - 1
            
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    if k > maxLen:
                        maxLen = k
                        start = i
        
        return s[start: start+maxLen]
