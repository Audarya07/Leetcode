from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counterDict = Counter(S)
        cnt = 0
        for val in J:
            if val in counterDict:
                cnt += counterDict[val]
        return cnt
        