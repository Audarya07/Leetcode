# Town Judge is basically a node with indegree == n-1 and outdegree == 0

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        cnts = [[0,0] for i in range(n+1)]  # [indegree, outdegree] pair for all nodes
        
        for u, v in trust:
            cnts[u][1] += 1     # outdegree_source++ 
            cnts[v][0] += 1     # indegree_dest++
        for i in range(n+1):
            if cnts[i][0] == n-1 and cnts[i][1] == 0:
                return i
        return -1