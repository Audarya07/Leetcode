from collections import Counter

# Solution 1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        ans = []
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        for val in set(nums1).intersection(nums2):
            ans.extend([val]*min(c1[val], c2[val]))

        return ans

# Solution 2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        c1 = Counter(nums1)
        
        for x in nums2:
            if x in c1 and c1[x] > 0:
                arr.append(x)
                c1[x] = c1[x] - 1
        return arr
    