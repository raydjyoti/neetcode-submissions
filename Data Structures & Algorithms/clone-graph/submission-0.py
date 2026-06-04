"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        store = {}

        def dfs(node):
            if not node: return node
            copy = None
            if node in store: return store[node]
            else:
                copy = Node(node.val)
                store[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
        
        return dfs(node)