class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for row in image:
            new_row=row[::-1]
            row=[]
            for cell in new_row:
                
                if cell==1:
                    row.append(0)
                else:
                    row.append(1)

            res.append(row)

        return res
        