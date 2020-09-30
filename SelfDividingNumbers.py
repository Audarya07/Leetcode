class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for val in range(left, right+1):
            dummy = val
            while val:
                rem = val % 10
                val //= 10
                if rem == 0 or dummy % rem != 0:
                    break
            else:
                ans.append(dummy)
        return ans