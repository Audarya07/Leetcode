class Solution:
    def countBits(self, num: int) -> List[int]:
        # Solution 1: O(32N)

        # ans = []
        # for val in range(num+1):
        #     bits = 0
        #     mask = 1
        #     for i in range(32):
        #         if val & mask != 0:
        #             bits += 1
        #         mask <<= 1        # left shift mask by 1 bit
        #     ans.append(bits)
        # return ans


        # Solution 2: O(N) --> Observation
        # If num is odd  --> cnt of set bit = 1 + cnt of set bits at num/2
        # If num is even --> cnt of set bit = cnt of set bits at num/2
        ans = [0]*(num+1)
        for i in range(1, num+1):
            ans[i] = ans[i//2] + (i%2)
        return ans