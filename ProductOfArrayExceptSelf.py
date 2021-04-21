# INPUT  = [4 5 1 8 2]
# OUTPUT = [80 64 320 160]

# Solution 1
# TC = O(N)
# SC = O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = [1]*n
        right_arr = [1]*n
        output_arr = [1]*n 
        
        for i in range(1, n):
            left_arr[i] = left_arr[i-1] * nums[i-1]		# [1 4 20 20 60]
        
        for i in range(n-2, -1, -1):
            right_arr[i] = right_arr[i+1] * nums[i+1]	# [80 16 16 2 1]
            
        for i in range(n):
            output_arr[i] = left_arr[i] * right_arr[i]
        
        return output_arr

# Solution 2
# TC = O(N)
# SC = O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output_arr = [1]*n 
        
        for i in range(1, n):
            output_arr[i] = output_arr[i-1] * nums[i-1]		# [1 4 20 20 60]
        
        right = 1
        for i in range(n-1, -1, -1):
            output_arr[i] = output_arr[i] * right
            right *= nums[i]
        
        return output_arr