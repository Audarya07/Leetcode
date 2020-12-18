class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')    # Positive infinity
        max_profit = 0
        for curr_val in prices:
            if curr_val < min_price:
                min_price = curr_val
            elif curr_val - min_price > max_profit:
                max_profit = curr_val - min_price
        return max_profit