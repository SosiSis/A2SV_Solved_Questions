from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        
        rows, cols = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        
        for r in range(rows):
            for c in range(cols):
                diagonals[r + c].append(mat[r][c])
        
        result = []
        
        for k in range(rows + cols - 1):
            if k % 2 == 0:
                
                result.extend(diagonals[k][::-1])
            else:

                result.extend(diagonals[k])
                
        return result