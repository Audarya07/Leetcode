# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. 
# The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.


import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def profit(x, y):
            return (x+1)/(y+1) - x/y
        
        heap = []
        for a, b in classes:
            heapq.heappush(heap, (-profit(a, b), a, b))
        
        for _ in range(extraStudents):
            avg, a, b = heapq.heappop(heap)
            heapq.heappush(heap, (-profit(a+1, b+1), a+1, b+1))
            
        return sum(a / b for d, a, b in heap) / len(classes)