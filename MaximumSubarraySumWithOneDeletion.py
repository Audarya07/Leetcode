class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0 for _ in range(n)]
        suf = [0 for _ in range(n)]
        ans = float('-inf')
        maxx = arr[0]
        
        pre[0] = arr[0]
        for i in range(1, n):
            if arr[i] + pre[i-1] >= arr[i]:
                pre[i] = arr[i] + pre[i-1]
            else:
                pre[i] = arr[i]
            maxx = max(maxx, pre[i])
                
        suf[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            if arr[i] + suf[i+1] >= arr[i]:
                suf[i] = arr[i] + suf[i+1]
            else:
                suf[i] = arr[i]
            maxx = max(maxx, suf[i])
            
        ans = maxx
        for i in range(1, n-1):
            ans = max(ans, pre[i-1]+suf[i+1])
                
        # print(pre)
        # print(suf)
        
        return ans
