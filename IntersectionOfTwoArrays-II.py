from collections import Counter

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
