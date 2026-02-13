class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows=len(img)
        cols=len(img[0])
        out=[[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                count=0
                sum=0

                for new_row in range(max(0,row-1),min(rows,row+2)):
                    for new_col in range(max(0,col-1),min(cols,col+2)):
                        count += 1
                        sum += img[new_row][new_col]
                out[row][col]=sum//count
        return out                