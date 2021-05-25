#left is a max heap --> max heap is implemented by pushing -num into the heap
#                       and accessing -ve of any value from the heap

#right is a min heap --> min heap is implemented by pushing +num into the heap
#                       and accessing the value itself from the heap


import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        
    def addNum(self, num: int) -> None:
        if len(self.left) == 0 or num < -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        if len(self.left) > len(self.right)+1:
            heapq.heappush(self.right, -self.left[0])
            heapq.heappop(self.left)
        elif len(self.right) > len(self.left)+1:
            heapq.heappush(self.left, -self.right[0])
            heapq.heappop(self.right)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0])/2
            
    
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()