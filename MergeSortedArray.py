class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if arr1[m-1] > arr2[n-1]:
                arr1[m+n-1] = arr1[m-1]
                m -= 1
            else:
                arr1[m+n-1] = arr2[n-1]
                n -= 1
            
        while n > 0:
            arr1[m+n-1] = arr2[n-1]
            n -= 1
