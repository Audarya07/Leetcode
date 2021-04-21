# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nmap = {}
        for val in nums2:
            while stack and val > stack[-1]:
                nmap[stack[-1]] = val
                stack.pop()
            stack.append(val)
        
        ans = []
        for val in nums1:
            if val in nmap:
                ans.append(nmap[val])
            else:
                ans.append(-1)
        return ans
                