class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i: [] for i in range(n)}
        visited = set()

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 0: [1], 1: [0, 2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1]
        # 0 -> 1 (p=0) -> 2 (p=1) -> 3 (2)

        def dfs(node, parent):
            
            if node in visited and node != parent: return False
            else: visited.add(node)

            edges = graph[node]

            for edge in edges:
                if edge == parent: continue
                if not dfs(edge, node): return False

            return True


        firstNode = 0
        parent = -1

        return dfs(firstNode, parent)



