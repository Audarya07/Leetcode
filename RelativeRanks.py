import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = []
        m = {0:"Gold Medal",1:"Silver Medal",2:"Bronze Medal"}
        
        for i in range(len(score)):
            heapq.heappush(arr, (-score[i],i))
            
        cnt = 0
        while arr:
            _,idx = heapq.heappop(arr)
            if cnt < 3:
                score[idx] = m[cnt]
            else:
                score[idx] = str(cnt+1)
            cnt += 1
            
        return score
