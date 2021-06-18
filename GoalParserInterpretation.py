class Solution:
    def interpret(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] == 'G':
                res.append(s[i])
            if s[i] == '(' and s[i+1] == 'a':
                res.append('a')
                res.append('l')
            if s[i] == '(' and s[i+1] == ')':
                res.append('o')
        
        return "".join(res)