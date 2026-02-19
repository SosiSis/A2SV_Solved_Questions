class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]<0:
                    res+=1
        return res