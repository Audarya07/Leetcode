# Input: n = 00000000000000000000000000001011
# Output: 3

# Input: n = 11111111111111111111111111111101
# Output: 31


# Solution 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            rem = n % 2
            n //= 2
            if rem == 1:
                cnt += 1
        return cnt

# Solution 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        mask = 1				# 00000000000000000000000000000001
        for i in range(32):
            if n & mask != 0:
                cnt += 1
            mask <<= 1 			# left shift mask by 1 - 00000000000000000000000000000010
        return cnt