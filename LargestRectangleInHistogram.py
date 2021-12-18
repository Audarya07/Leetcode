class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        left_small = [0 for i in range(n)]
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if not stack:
                left_small[i] = 0
            else:
                left_small[i] = stack[-1] + 1
            stack.append(i)
        
        while stack:
            stack.pop()
            
        right_small = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if not stack:
                right_small[i] = n-1
            else:
                right_small[i] = stack[-1] - 1
            stack.append(i) 
        
        ans = 0
        for i in range(n):
            ans = max(ans, nums[i]*(right_small[i] - left_small[i] + 1))

        return ans
