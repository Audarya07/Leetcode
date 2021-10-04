# Given two strings word1 and word2, return the minimum number of operations 
# required to convert word1 to word2.

# You have the following three operations permitted on a word:
#     Insert a character
#     Delete a character
#     Replace a character

 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3

# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # row contains word1
        # column contains word2
        # dp[i][j] = number of ways to convert substr1 to substr2 using the minimum of the given 3 operations        
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        if word1 == "":
            return len(word2)
        
        if word2 == "":
            return len(word1)
        
        # fill 1st column
        for i in range(len(word1)+1):
            dp[i][0] = i
            
        # fill 1st row
        for j in range(len(word2)+1):
            dp[0][j] = j
        
        # fill rest matrix
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[len(word1)][len(word2)]
    
    # insert = move left + 1 --> dp[i][j-1]
    # delete = move up + 1 --> dp[i-1][j]
    # replace = move upper left diagonal + 1 --> dp[i-1][j-1]
    # take min of these 3 operations to get value of a cell
    