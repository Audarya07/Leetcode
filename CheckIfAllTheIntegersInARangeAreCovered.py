class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # TC = O(N*R)
        # flag = 1
        # for x in range(left, right+1):
        #     for i in range(len(ranges)):
        #         if x >= ranges[i][0] and x <= ranges[i][1]:
        #             flag = 1
        #             break
        #         else:
        #             flag = 0
        #     if flag == 0:
        #         return False
        # return True
        
        # TC = O(N+R)
        vis = [0]*55
        for s, e in ranges:
            vis[s] += 1
            vis[e + 1] -= 1
        for i in range(1, len(vis)):
            vis[i] += vis[i-1]
        for i in range(left, right + 1):
            if vis[i] == 0:
                return False
        return True