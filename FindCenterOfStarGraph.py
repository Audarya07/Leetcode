class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center of graph will be a node common to all other nodes
        # THat means it will be common in edges[0] and edges[1] also
        e1, e2 = edges[0]
        return e1 if e1 in edges[1] else e2