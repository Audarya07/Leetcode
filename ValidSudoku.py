# Solution 1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            cube = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    else:
                        col.add(board[j][i])
                ridx = 3 * (i//3)
                cidx = 3 * (i%3)
                if board[ridx + j//3][cidx + j%3] != '.':
                    if board[ridx + j//3][cidx + j%3] in cube:
                        return False
                    else:
                        cube.add(board[ridx + j//3][cidx + j%3])
        return True


# Solution 2
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridSet = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    val = board[i][j]
                    if (i,val) in gridSet or (val,j) in gridSet or (i//3,j//3,val) in gridSet:
                        return False
                    gridSet.add((i,val))
                    gridSet.add((val,j))
                    gridSet.add((i//3,j//3,val))
        return True
