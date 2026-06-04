class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowStore = dict()
        colStore = dict()
        gridStore = dict()

        def gridFind(row, col):
            if (row < 3):
                if (col < 3): return 0
                elif (col >=3 and col < 6): return 1
                else: return 2
            elif (row >= 3 and row < 6):
                if (col < 3): return 3
                elif (col >=3 and col < 6): return 4
                else: return 5
            else:
                if (col < 3): return 6
                elif (col >=3 and col < 6): return 7
                else: return 8

        def rowCheck(row, num):
            if (row not in rowStore):
                rowStore[row] = set([num])
                return False
            if (num in rowStore[row]): return True
            else:
                rowStore[row].add(num)
                return False

        def colCheck(col, num):
            if (col not in colStore):
                colStore[col] = set([num])
                return False
            if (num in colStore[col]): return True
            else:
                colStore[col].add(num)
                return False

        def gridCheck(grid, num):
            if (grid not in gridStore):
                gridStore[grid] = set([num])
                return False
            if (num in gridStore[grid]): return True
            else:
                gridStore[grid].add(num)
                return False

        for i in range(len(board)):
            row = i

            for j in range(len(board[row])):
                col = j
                num = board[row][col]

                if (num == "."): continue

                if (rowCheck(row, num)): return False
                if (colCheck(col, num)): return False

                gridNum = gridFind(row, col)

                if (gridCheck(gridNum, num)): return False

        return True


