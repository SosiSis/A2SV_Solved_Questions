class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map=defaultdict(str)
        for person,height in zip(names,heights):
            map[height]=person

        for height in range(len(heights)):
            for other_height in range(height+1,len(heights)):
                if heights[height] < heights[other_height]:
                    heights[height] , heights[other_height]=heights[other_height],heights[height]  
       
        res=[]
        for height in heights:
          res.append(map[height])
        return res   