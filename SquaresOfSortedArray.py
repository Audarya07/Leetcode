class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [i*i for i in A]
        return sorted(ans)