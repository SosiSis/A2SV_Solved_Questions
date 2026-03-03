class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):

            for c in range(COLS):
               
                self.sumMat[r][c] = matrix[r][c] + self.sumMat[r-1][c] + self.sumMat[r][c-1] -self.sumMat[r-1][c-1]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1

        # bottomRight = self.sumMat[r2][c2]
        # above = self.sumMat[r1 - 1][c2]
        # left = self.sumMat[r2][c1 - 1]
        # topLeft = self.sumMat[r1 - 1][c1 - 1]
        box= self.sumMat[r2][c2]
        left_box=self.sumMat[r2][c1-1]
        up_box=self.sumMat[r1-1][c2]
        overlap = self.sumMat[r1-1][c1-1]


        # return bottomRight - above - left + topLeft  
        return box - left_box - up_box + overlap  


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)