# Given two strings s and t, return the minimum window in s 
# which will contain all the characters in t.
# If there is no such window in s that covers all characters in t,
# return the empty string "".
# Input:
# s = "ADOBECODEBANC"
# t = "ABC"
# Output = "BANC"


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Two pointer approch -> both l & r start from same side of list
        tmap = Counter(t)
        ans = s + "!"           #initially ans should be somthing impossible for comparison
        cmap = {}
        for c in tmap.keys():
            cmap[c] = 0

        ccount = 0
        tcount = len(t)
        l, r = 0, 0

        while r < len(s):
            c = s[r]
            if c in tmap:
                cmap[c] += 1
                if cmap[c] <= tmap[c]:      #curr char cnt is less than required char cnt 
                    ccount += 1
                # while loop to check if we can shift 'l' forward
                while l < r and (s[l] not in tmap or cmap[s[l]] > tmap[s[l]]):
                    if tmap[s[l]]:
                        cmap[s[l]] -= 1
                    l += 1              # if s[l] not in tmap -> ignore and incr. 'l'
                if tcount == ccount:
                    ans = ans if len(ans) <= r-l+1 else s[l:r+1]
            r += 1          # skip s[r] and move forward

        return ans if len(ans) <= len(s) else ""
