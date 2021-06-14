class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        m = [0]*26
        for x in sentence:
            m[ord(x)-97] += 1
        for x in m:
            if x == 0:
                return False
        return True