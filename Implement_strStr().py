# Input: haystack = "hello", needle = "ll"
# Output: 2  --> index of the first occurrence of needle

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len = len(haystack)
        need_len = len(needle)
        
        # loop to slide needle one by one
        for i in range(hay_len - need_len + 1):
            j = 0
            
            # loop to match needle for curr value of i
            while j < len(needle):
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            
            if j == need_len:
                #matched the needle
                return i
        return -1
            