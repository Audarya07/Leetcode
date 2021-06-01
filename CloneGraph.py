# Problem Statement:
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copy = defaultdict(Node)
        
        def helper(node):
            if not node:
                return None
            
            if node.val not in copy.keys():
                copy[node.val] = Node(node.val, [])
                for x in node.neighbors:
                    copy[node.val].neighbors.append(helper(x))

            return copy[node.val]
        
        return helper(node)