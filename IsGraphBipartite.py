class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #nodes connected across an edge should have different color
        
        n = len(graph)
        col = [-1]*n
        for i in range(n):
            if col[i] != -1:
                continue
            queue = [i]
            # 'g'->green, b->blue
            col[i] = "g"
            while len(queue) != 0:
                node = queue.pop(0)
                for x in graph[node]:
                    if col[x] == -1:
                        if col[node] == "b":
                            col[x] = "g"
                        elif col[node] == "g":
                            col[x] = "b"
                        queue.append(x)
                    elif col[x] == col[node]:
                        return False
        return True
    