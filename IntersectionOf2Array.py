from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Solution 1
        # arr = Counter(nums1)
        # ans = []
        # for val in nums2:
        #     if val in arr and val not in ans:
        #         ans.append(val)
        # return ans
        
        #Solution 2
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)