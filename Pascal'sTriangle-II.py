class Solution:
    def getRow(self, n: int) -> List[int]:
        res = [[1]]
          
        for i in range(n):
            row = []
            row.append(1)
            for j in range(len(res[i])-1):
                row.append(res[i][j] + res[i][j+1])
            row.append(1)
            res.append(row)
        
        return res[-1]
