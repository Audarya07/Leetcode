class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        empty = 1
        self.unique_path = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    s_i = i
                    s_j = j
                if grid[i][j] == 0:
                    empty += 1
        
        def dfs(x, y, empty):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] < 0:
                return 0
            if grid[x][y] == 2:
                if empty == 0:
                    self.unique_path += 1
                return 
            grid[x][y] = -2
            empty -= 1
            dfs(x+1, y, empty)
            dfs(x-1, y, empty) 
            dfs(x, y+1, empty) 
            dfs(x, y-1, empty)
            grid[x][y] = 0
            empty += 1
            
        
        dfs(s_i, s_j, empty)
        return self.unique_path