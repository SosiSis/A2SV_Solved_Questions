class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for list in matrix:
            low=0
            high=len(list)-1
            while low<=high:
                mid=(low+high)//2
                if list[mid]==target:
                    return True
                elif list[mid] < target:
                    low=mid+1
                    
                else:
                    high=mid-1
        return False                    