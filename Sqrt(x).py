# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated,
# and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 1
        r = x
        while l <= r:
            mid = l + (r-l) // 2
            if mid == x//mid:
                return mid
            elif mid < x/mid:
                l = mid + 1
            else:
                r = mid - 1
        return r
        