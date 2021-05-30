# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]


# BFS Solution
class Solution:
    def bfs_cycle(self, n, mp, u, v):
        vis = [0]*(n+1)
        q = [u]
        
        while len(q) != 0:
            node = q.pop(0)
            vis[node] = 1
            if node == v:
                return True
            for e in mp[node]:
                if vis[e] == 0:
                    q.append(e)

        return False
                
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        mp = defaultdict(list)
        
        for e in edges:
            if self.bfs_cycle(n, mp, e[0], e[1]):
                return e
            mp[e[0]].append(e[1])
            mp[e[1]].append(e[0])
            
##############################################################################

# DFS Solution 
from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        mp = defaultdict(set)
        
        def dfs(u, v):
            if u == v:
                return True
            
            if vis[u] == 0:
                vis[u] = 1
                for x in mp[u]:
                    if dfs(x, v):
                        return True
            return False
        
        for u, v in edges:
            vis = [0]*(n+1)
            if dfs(u, v):
                return [u, v]
            mp[u].add(v)
            mp[v].add(u)
        