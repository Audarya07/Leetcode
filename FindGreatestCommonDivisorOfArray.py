class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = float('inf')
        mx = float('-inf')        
        
        # Find min and max present in nums
        for val in nums:
            if val > mx:
                mx = val
            if val < mn:
                mn = val
        
        # default max divisor
        maxx = 1       
        for x in range(1, mn+1):
            if mx % x == 0 and mn % x == 0 and x > maxx:
                maxx = x
        
        if maxx:
            return maxx
        return 1


# Solution 2 based on Euclidean Algo
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        while a:
            a, b = b % a, a
        return b
