class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # To find index of smallest element
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r)//2
            if nums[mid] >= nums[r]:        # [4,5,6,7,0,1,2]
                l = mid + 1
            else:
                r = mid
        
        start = l       # store the index of smallest element in var start 
        l = 0
        r = len(nums) - 1
        
        # set the l and r for searching the target
        if target >= nums[start] and target <= nums[r]:
            l = start
        else:
            r = start
             
        # Searching in the specified range by normal binary search
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1