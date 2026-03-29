class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> None:
            if row == n:
                nonlocal solution_count
                solution_count += 1
                return
          
            for col in range(n):
           
                diagonal_idx = row + col
                anti_diagonal_idx = row - col + n
              
                if columns_used[col] or diagonals_used[diagonal_idx] or anti_diagonals_used[anti_diagonal_idx]:
                    continue
              
                columns_used[col] = True
                diagonals_used[diagonal_idx] = True
                anti_diagonals_used[anti_diagonal_idx] = True
              
                backtrack(row + 1)
              
                columns_used[col] = False
                diagonals_used[diagonal_idx] = False
                anti_diagonals_used[anti_diagonal_idx] = False
      
        
        columns_used = [False] * n  
        diagonals_used = [False] * (2 * n)  
        anti_diagonals_used = [False] * (2 * n)  
      
        solution_count = 0
      
        backtrack(0)
      
        return solution_count