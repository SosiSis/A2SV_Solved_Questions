class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
            def min_dist(house,heaters):
                heaters.sort()
                left,right=0,len(heaters) -1
                min_dist=float(inf)
                while left <= right:
                    mid = (left + right) // 2
                    min_dist=min(min_dist,abs(heaters[mid]-house))
                    if heaters[mid] > house:
                        right=mid-1
                    elif heaters[mid]<house:
                        left=mid +1
                    else:
                        return 0    
                return min_dist
            min_range=0
            for house in houses:
                min_range=max(min_range,min_dist(house,heaters))
            return min_range    



