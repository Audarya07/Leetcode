class Solution:
    def canFinish(self, numCourses: int, graph: List[List[int]]) -> bool:
        # Topological sort of a Graph
        # 1. check nodes whose indegree == 0 and add them to ans
        # 2. remove these nodes from graph
        # 3. then remove the outgoing edges from the deleted node
        # 4. if there exists a node where indegree != 0 ---> cycle exists
        # 5. else no cycle ---> topological sort is successful
        
        outdegree = defaultdict(set)
        indegree = [0]*numCourses
        
        # Here, if pair is [u, v] means u is dependent on v
        # so edge goes from v -> u
        for u, v in graph:
            indegree[u] += 1
            outdegree[v].add(u)
        
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
                
        edge_cnt = len(graph)
        while len(stack) != 0:
            node = stack.pop()
            for x in outdegree[node]:
                edge_cnt -= 1
                indegree[x] -= 1
                if indegree[x] == 0:
                    stack.append(x)
        
        return edge_cnt == 0