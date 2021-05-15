from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1
        ans = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            ans[tuple(cnt)].append(s)
        return ans.values()
        
        # Solution 2
        # res = defaultdict(list)
        # for s in strs:
        #     val = "".join(sorted(s))
        #     res[val].append(s)
        # return res.values()