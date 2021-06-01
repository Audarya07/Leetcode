# Given a string s, partition s such that every substring of the partition 
# is a palindrome. Return all possible palindrome partitioning of s.


# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def backtrack(ans, curr, s, start):
            if start == len(s):
                ans.append(curr[:])
            for i in range(start, len(s)):
                tmp = s[start: i+1]
                if tmp == tmp[::-1]:
                    curr.append(tmp)
                    backtrack(ans, curr, s, i+1)
                    curr.pop()
                    
        backtrack(ans, [], s, 0)
        return ans

# TC = O(N*(2**N))  
# there are 2**N s=ubstring possible and each substring requires O(N) time
# to traverse and check if it's palindrome or not 

# SC = O(N) -->  space will be used to store the recursion stack
# depth of stack = len(s) = N