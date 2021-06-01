# Vertices whose indegree == 0 will help to reach all nodes of graph

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        cnts = [0]*n  # [indegree, outdegree] pair for all nodes
        ans = []
        
        for u, v in edges:
            cnts[v] += 1     # indegree_dest++
            
        for x in range(n):
            if cnts[x] == 0:
                ans.append(x)
        return ans