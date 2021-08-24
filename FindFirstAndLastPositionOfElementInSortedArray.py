class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def locate(x):
            l, r = 0, len(nums)           
            while l < r:
                m = (l + r) // 2
                if nums[m] < x:
                    l = m + 1
                else:
                    r = m                    
            return l
        
        left = locate(target)
        right = locate(target+1) - 1
        
        return [left, right] if left <= right else [-1, -1]