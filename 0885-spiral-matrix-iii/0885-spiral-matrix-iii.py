class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:

        res = [[rStart, cStart]]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        r, c = rStart, cStart
        steps = 1  
        d = 0      
        
        while len(res) < rows * cols:
    
            for _ in range(2):
                for _ in range(steps):
                    r += dr[d]
                    c += dc[d]
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    
                    if len(res) == rows * cols:
                        return res
                
                d = (d + 1) % 4
    
            steps += 1
            
        return res