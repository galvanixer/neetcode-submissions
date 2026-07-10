class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Valid row checker
        nrows = len(board)
        ncols = len(board[0])

        for i in range(nrows):
            seenrow = set()
            for j in range(ncols):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seenrow:
                    return False
                seenrow.add(board[i][j])

        for j in range(ncols):
            seencol = set()
            for i in range(nrows):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seencol:
                    return False
                seencol.add(board[i][j])

        for sqidx in range(9):
            seensquare = set()
            for i in range(3):
                row = sqidx//3 + i
                for j in range(3):
                    col = (sqidx//3)*3 + j
                    print(f"sqidx: {sqidx} row: {row}, col: {col}")
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seensquare:
                        return False
                    seensquare.add(board[row][col])

        return True