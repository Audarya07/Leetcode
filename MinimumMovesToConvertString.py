class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        cnt = 0
        while i < len(s):
            if s[i] == 'O':
                i += 1
            else:
                cnt += 1
                i += 3
        return cnt
