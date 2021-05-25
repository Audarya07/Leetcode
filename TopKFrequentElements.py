import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        heap = []
        for num, cnt in cntr.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]