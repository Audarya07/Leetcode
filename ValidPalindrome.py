# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Solution 1 
#         s = "".join(c.lower() for c in s if c.isalnum())
#         if s == s[::-1]:
#             return True
#         return False
    
    
        # Solution 2
        i, j = 0, len(s)-1
        while i < j:
            while s[i].isalnum() == False and i < j:
                i += 1
            while s[j].isalnum() == False and i < j:
                j -= 1
            if(s[i].lower() != s[j].lower()):
                return False
            i += 1
            j -= 1
        return True