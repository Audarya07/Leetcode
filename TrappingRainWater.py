# Solution 1 : Using 2 pointer approach

class Solution:
    def trap(self, h: List[int]) -> int:
        left_max = 0
        right_max = 0
        l = 0
        r = len(h) - 1
        ans = 0
        while l < r:
            if h[l] < h[r]:
                if h[l] >= left_max:
                    left_max = h[l]
                else:
                    ans += (left_max - h[l])
                l += 1
            else:
                if h[r] >= right_max:
                    right_max = h[r]
                else:
                    ans += (right_max - h[r])
                r -= 1
        return ans