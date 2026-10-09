class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Case 1: Check row for no duplicates 
        # AND
        # Case 2: Check column for no duplicates
        # AND
        # Case 3: Check 3X3 room has no duplicates

        # Case 1: Check rows for no duplicates
        
        for i in range(9):
            row_hash = [0] * 10
            for j in range(9):

                if board[i][j] != '.' and row_hash[int(board[i][j])] == 0:
                    row_hash[int(board[i][j])] = row_hash[int(board[i][j])] + 1 
                elif board[i][j] != '.' and row_hash[int(board[i][j])] == 1:
                    return False
        # Case 2: Check column for no duplicates
        for j in range(9):
            col_hash = [0] * 10
            for i in range(9):
                if board[i][j] != '.' and col_hash[int(board[i][j])] == 0:
                    col_hash[int(board[i][j])] = col_hash[int(board[i][j])] + 1 
                elif board[i][j] != '.' and col_hash[int(board[i][j])] == 1:
                    return False
        
        # Case 3: Check 3X3 room has no duplicates
        # To identify row and colum
        # Top right 3X3 cell: row = ceil((i+1)/3)
        # i j [0, 0], [0, 3], [0, 6]
        #     [3, 0], [3, 3], [3, 6]
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                mat_hash = [0] * 11
                counter = 0
                for k in range(3):
                    for l in range(3):
                        row, col = i + k, j + l
                        # print(row, col, board[row][col])
                        if board[row][col] != '.' and mat_hash[int(board[row][col])-1] == 0:
                            mat_hash[int(board[row][col])-1] = mat_hash[int(board[row][col])-1] + 1 
                            print(board[row][col], k, l, mat_hash, counter, mat_hash[counter])

                            counter = counter + 1
                        elif board[row][col] != '.' and mat_hash[int(board[row][col])-1] == 1: 
                            print(board[row][col], k, l, mat_hash, counter, mat_hash[counter])
                            
                            counter = counter + 1
                            return False
                        
                        # counter = counter + 1
        return True


        