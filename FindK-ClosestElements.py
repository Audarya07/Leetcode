# Solution 1: O(Nlog(N)) - Custom Sorting
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort(key=lambda val: abs(x - val))
        ans = []
        for i in range(k):
            ans.append(arr[i])
        return sorted(ans)

# Optimal solution
# Solution 2: O(Nlog(k) + klog(k)) = O(Nlog(k)) - MaxHeap
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Solution MaxHeap
        mx_heap = []
        res = []
        for i in range(len(arr)):
            gap = abs(arr[i] - x)
            if len(mx_heap) < k:
                heapq.heappush(mx_heap, (-gap, -arr[i]))
            else:
                if mx_heap[0][0] < -gap:
                    heapq.heappop(mx_heap)
                    heapq.heappush(mx_heap, (-gap, -arr[i]))
        
        for i in range(len(mx_heap)):
            # reverse the -ve sign again to retain original value
            res.append(-heapq.heappop(mx_heap)[1])
            
        return sorted(res)
    


# Some problem exsist in the solution for some test cases but mostly works
# Solution 3: O(log(N) + k) - Binary search and 2 Pointer
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        if len(arr) == k:
            return arr
        
        l = 0
        r = len(arr) - 1
        mid = 0
        while l <= r:
            mid = (l+r)//2
            if arr[mid] > x:
                r = mid - 1
            elif arr[mid] < x:
                l = mid + 1
            else:
                break

        # l holds index of closest element to x...so we set l & r for creating the window
        l = l - 1
        r = l + 1
        
        while r-l-1 < k:
            # To avoid out of bounds on left side
            if l == -1:
                r += 1
                continue
            # To avoid out of bounds on right side
            if r == len(arr) or abs(x - arr[l]) <= abs(x - arr[r]):
                l -= 1
            else:
                 r += 1

        for i in range(l+1, r):
            ans.append(arr[i])
        return ans
       