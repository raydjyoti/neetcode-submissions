class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        vistedPacific = set()
        visitedAtlantic = set()

        self.row = len(heights)
        self.col = len(heights[0])

        def dfs(r, c, prevHeight, ocean):

            if r < 0 or c < 0 or r >= self.row or c >= self.col:
                return
            

            if prevHeight > heights[r][c]: return

            if ocean == "atlantic":
                if (r,c) in visitedAtlantic: return
                visitedAtlantic.add((r,c))

            elif ocean == "pacific":
                if (r,c) in vistedPacific: return
                vistedPacific.add((r,c))

            directions = [[-1, 0], [1,0], [0, -1], [0, 1]]

            for row, col in directions:
                newRow = r+row
                newCol = c+col

                dfs(newRow, newCol, heights[r][c], ocean)

        for r in range(self.row):
            # Go from Pacific -> Atlantic, Left to Right
            dfs(r, 0, heights[r][0], "atlantic")
            
            # Go from Atlantic -> Pacific, Right to Left
            dfs(r, self.col-1, heights[r][self.col-1], "pacific")

        for c in range(self.col):
            # Go from Pacific -> Atlantic, Top to Bottom
            dfs(0, c, heights[0][c], "atlantic")

            # Go from Atlantic -> Pacific, Bottom to Top
            dfs(self.row-1, c, heights[self.row-1][c], "pacific")
        
        return list(visitedAtlantic & vistedPacific)