class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}
        for x, y in zip(s, t):
            if x not in s_to_t and y not in t_to_s:
                s_to_t[x] = y
                t_to_s[y] = x
                
            elif s_to_t.get(x) != y or t_to_s.get(y) != x:
                return False
        return True
    
            