class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = len(bin(n)[2:])
        return (2**num - 1) - n