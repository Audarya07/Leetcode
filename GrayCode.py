class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Solution 1 = O(n * 2^n)
        # res = [0]
        # vis = set()
        # vis.add(0)
        
        # def helper(res, n, vis):
        #     if len(res) == (1 << n):
        #         return True
        #     curr = res[-1]
        #     for i in range(n):
        #         nxt = curr ^ (1 << i)
        #         if nxt not in vis:
        #             res.append(nxt)
        #             vis.add(nxt)
        #             if helper(res, n, vis):
        #                 return True
        #             else:
        #                 vis.remove(nxt)
        #                 res.pop()
        #     return False
        
        # helper(res, n, vis)
        # return res

        # Solution 2 = O(n * 2^n) time
        res = [0]
        vis = set()
        vis.add(0)
        
        for _ in range(1 << n):
            for x in range(n):
                if (1 << x) ^ res[-1] not in vis:
                    nxt = (1 << x) ^ res[-1]
                    vis.add(nxt)
                    res.append(nxt)
                    break
        return res
        #     