import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x in points:
            # we implement max heap in python by negating the value to be pushed in heap
            dist = -x[0]**2 -x[1]**2        
            if len(heap) < k:
                heapq.heappush(heap, (dist, x))
            else:
                if dist > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (dist, x))
                
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
            
# TC = O(NlogK)