class Solution(object):
    def isValidSudoku(self, board):
        # For checking uniqueness of row, use store
        # For column, use store
        # Store => {r1: [set], r2, r3..., c1, c2, c3}
        # Store => {sb1: [set], sb2, ... sb9}
        # To know what sub-box, rows = i, cols = j
        # sb1 range = row < 4 && col < 4,
        # sb2 range = row < 4, col > 4 && col < 7

        store = {}


        def sbCal(row, col):
            if (row <= 3):
                if (col <= 3): return "sb1"
                elif (col > 3 and col <= 6): return "sb2"
                elif (col > 6 and col <= 9): return "sb3"

            if (row > 3 and row <= 6):
                if (col <= 3): return "sb4"
                elif (col > 3 and col <= 6): return "sb5"
                elif (col > 6 and col <= 9): return "sb6"
            if (row > 6 and row <= 9):
                if (col <= 3): return "sb7"
                elif (col > 3 and col <= 6): return "sb8"
                elif (col > 6 and col <= 9): return "sb9"
            


        for i in range(len(board)):
            row = i+1

            for j in range(len(board[i])):
                col = j+1
                currNum = board[i][j]

                if (currNum == "."): continue

                rowCode = f"r{row}"
                colCode = f"c{col}"
                sbCode = sbCal(row, col)

                if (rowCode not in store): store[rowCode] = set()
                if (colCode not in store): store[colCode] = set()
                if (sbCode not in store): store[sbCode] = set()

                print(store)

                if (currNum in store[rowCode]): return False
                else: store[rowCode].add(currNum)

                if (currNum in store[colCode]): return False
                else: store[colCode].add(currNum)

                if (currNum in store[sbCode]): return False
                else: store[sbCode].add(currNum)
                
        return True
        