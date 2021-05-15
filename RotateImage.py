Input:  [[1,2,3],
         [4,5,6],
         [7,8,9]]

Output: [[7,4,1],
         [8,5,2],
         [9,6,3]]


class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m)
        # transpose
        for i in range(n):
            for j in range(i, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]
                
        # reverse the rows
        for i in range(n):
            for j in range(n//2):
                m[i][j], m[i][n-j-1] = m[i][n-j-1], m[i][j]