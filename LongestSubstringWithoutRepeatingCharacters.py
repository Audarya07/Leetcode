# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        i, j = 0, 0
        cset = set()
        n = len(s)
        while j < n:
            if s[j] not in cset:
                cset.add(s[j])
                j += 1
                cnt = max(cnt, j-i)
            else:
                cset.remove(s[i])
                i += 1
        return cnt
                