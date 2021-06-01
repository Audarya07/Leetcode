class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(set)
        dist = [float('inf')]*(n+1)
        for u, v, w in times:
            adj[u].add((v, w))     # {from1:(to1, weight1), from2:(to2, weight2)}
            
        queue = [(0, k)]       # [(min_dist, node)]
        dist[k] = 0            # dist of src node to itself = 0
        
        res = 0
        
        while len(queue) != 0:
            time, node = queue.pop(0)
            dist[node] = min(dist[node], time)
            
            for v, w in adj[node]:
                if w + time < dist[v]:
                    queue.append((w + time, v))
        
        for i in range(1, n+1):
            # if any node is unvisited return -1
            if dist[i] == float('inf'):
                return -1
            # else res = max(dist) --> min time needed for signal to reach all nodes
            res = max(res, dist[i])
        return res