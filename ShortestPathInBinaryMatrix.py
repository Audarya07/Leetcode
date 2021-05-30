# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirxn = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        if grid[0][0] or grid[-1][-1]:
            return -1
        grid[0][0] = 1
        q = [(0,0,1)]
        
        for x, y, cnt in q:
            if x == n-1 and y == n-1:
                return cnt
            for i, j in dirxn:
                if x+i >=0 and x+i < n and y+j >=0 and y+j < n and grid[x+i][y+j] == 0:
                    grid[x+i][y+j] = 1
                    q.append((x+i, y+j, cnt+1))
        return -1