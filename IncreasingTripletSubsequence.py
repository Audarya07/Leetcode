class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        
        n1 = nums[0]
        n2 = None
        for i in range(1, len(nums)):
            if nums[i] <= n1:
                n1 = nums[i]
            else:
                if n2 != None and nums[i] > n2:
                    return True
                n2 = nums[i]
            
        return False


# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         n1 = n2 = float('inf')
#         for n in nums:
#             if n <= n1:
#                 n1 = n
#             elif n <= n2:
#                 n2 = n
#             else:
#                 return True
#         return False