class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        j = 9
        d = {}
        while i < j and j < len(s):
            # print(s[i:j+1])
            if s[i:j+1] not in d.keys():
                d[s[i:j+1]] = 1
            else:
                d[s[i:j+1]] += 1
            i += 1
            j += 1
            
        ans = []
        for k, v in d.items():
            if v > 1:
                ans.append(k)
        return ans