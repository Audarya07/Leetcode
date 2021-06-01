class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        mx = 0
        
        def dfs(r, c):
            if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and (r,c) not in vis and grid[r][c]):
                return 0
            vis.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = dfs(r,c)
                mx = max(mx, val)
        return mx