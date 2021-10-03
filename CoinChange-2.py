# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1



# Brute Force approach
# Time complexity: O(N * 2^N) 
class Solution:   
    def changeRecursive(self, amt, coins, index):
        if amt == 0:
            return 1
        
        if index >= len(coins):
            return 0
        
        include = 0
        exclude = 0
        
        if coins[index] <= amt:
            include = self.changeRecursive(amt-coins[index], coins, index)
        exclude = self.changeRecursive(amt, coins, index+1)
        
        return include + exclude
    
    def change(self, amount: int, coins: List[int]) -> int:
        return self.changeRecursive(amount, coins, 0)


# DP Top Down Approach
# Time Complexity: O(N^2) --> (num of coins * amount)
class Solution:   
    def changeRecursive(self, amt, coins, index, dp):
        if amt == 0:
            return 1
        
        if index >= len(coins):
            return 0
        
        if dp[index][amt] != -1:
            return dp[index][amt]
        
        include = 0
        exclude = 0
        
        if coins[index] <= amt:
            include = self.changeRecursive(amt-coins[index], coins, index, dp)
        exclude = self.changeRecursive(amt, coins, index+1, dp)
        
        dp[index][amt] = include + exclude

        return dp[index][amt]
    
    
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for j in range(amount+1)] for i in range(len(coins))]
        return self.changeRecursive(amount, coins, 0, dp)


# DP Bottom Up Approach
# Time complexity: O(N^2)
class Solution:   
    # DP Bottom Up approach
    def change(self, amount: int, coins: List[int]) -> int:
        # coins as row
        # 0 to amt as columns
        dp = [[-1 for j in range(amount+1)] for i in range(len(coins)+1)]

        for i in range(len(coins)+1):
            dp[i][0] = 1
            
        for j in range(1, amount+1):
            dp[0][j] = 0
            
            
        for curr_coin in range(1, len(coins)+1):
            for curr_amt in range(1, amount+1):
                if coins[curr_coin-1] <= curr_amt:
                    dp[curr_coin][curr_amt] = dp[curr_coin][curr_amt-coins[curr_coin-1]] + dp[curr_coin-1][curr_amt]
                else:
                    dp[curr_coin][curr_amt] = dp[curr_coin-1][curr_amt]

        return dp[len(coins)][amount]
    



















