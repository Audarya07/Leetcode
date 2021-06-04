class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bfs(grid):
            queue = []
            fresh = 0
            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        queue.append((i,j))
                    elif grid[i][j] == 1:
                        fresh += 1    
            minutes = 0
            
            while len(queue) != 0 and fresh > 0:
                minutes += 1
                for _ in range(len(queue)):
                    x, y = queue.pop(0)
                    for i, j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                            continue
                        if grid[i][j] == 1:
                            grid[i][j] = 2
                            fresh -= 1
                            queue.append((i, j))
                            
            return minutes if fresh == 0 else -1
        
        return bfs(grid)