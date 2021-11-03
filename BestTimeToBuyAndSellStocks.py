# Solution 1
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


# Solution 2
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        arr = [0 for i in range(len(nums))]
        minn = nums[0]
        profit = 0
        for i in range(1, len(nums)):
            if nums[i] < minn:
                minn = nums[i]
            
            curr = nums[i] - minn
            if curr > profit:
                profit = curr
            arr[i] = profit
            
        return arr[-1]
