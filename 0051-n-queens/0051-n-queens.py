from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col):
            # Check the same column
            if col in columns:
                return False
            # Check the main diagonal (row - col should be unique)
            if (row - col) in diagonals1:
                return False
            # Check the anti-diagonal (row + col should be unique)
            if (row + col) in diagonals2:
                return False
            return True
        
        def backtrack(row):
            # If we've placed queens on all rows, add the board to the results
            if row == n:
                board = ["".join(row) for row in current_board]
                result.append(board)
                return
            
            for col in range(n):
                if is_safe(row, col):
                    # Place the queen
                    current_board[row][col] = 'Q'
                    columns.add(col)
                    diagonals1.add(row - col)
                    diagonals2.add(row + col)
                    
                    # Move on to the next row
                    backtrack(row + 1)
                    
                    # Backtrack: Remove the queen
                    current_board[row][col] = '.'
                    columns.remove(col)
                    diagonals1.remove(row - col)
                    diagonals2.remove(row + col)
        
        result = []
        current_board = [['.' for _ in range(n)] for _ in range(n)]
        columns = set()
        diagonals1 = set()  # main diagonal (row - col)
        diagonals2 = set()  # anti-diagonal (row + col)
        backtrack(0)
        return result
