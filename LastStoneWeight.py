#heapq is a min heap...we need max heap, so we negate all values initially
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-x for x in stones]
        heapq.heapify(arr)
        while len(arr) > 1:
            val1 = heapq.heappop(arr)
            val2 = heapq.heappop(arr)
            diff = val1 - val2
            heapq.heappush(arr, diff)
        return -arr[0]