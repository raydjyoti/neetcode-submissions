from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = set()
        islands = 0

        def bfs(i, j):
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            q = deque()
            q.append((i,j))

            while q:
                curr = q.popleft()

                for row, col in directions:
                    newRow = curr[0]+row
                    newCol = curr[1]+col

                    if (newRow, newCol) in visited: continue
                    else: visited.add((newRow, newCol))

                    if newRow >= len(grid) or newRow < 0 or newCol >= len(grid[0]) or newCol < 0:
                        continue

                    if grid[newRow][newCol] == "1":
                        q.append((newRow, newCol))

                    


        for i in range(row):
            for j in range(col):

                if grid[i][j] == "1" and (i,j) not in visited:
                    islands+=1
                    visited.add((i,j))
                    bfs(i,j)

        return islands

