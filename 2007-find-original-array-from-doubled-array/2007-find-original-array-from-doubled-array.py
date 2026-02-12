class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) % 2 != 0:
            return []
        
        
        counts = Counter(changed)
        
        keys = sorted(counts.keys())
        original = []
        for x in keys:
         
            if counts[x] == 0:
                continue
            
            count_of_x = counts[x]
            if counts[x] > counts[x * 2]:
                return []
            
            if x == 0:
                if count_of_x % 2 != 0:
                     return []
                original.extend([0] * (count_of_x // 2))
                counts[0] = 0 
            else:
                original.extend([x] * count_of_x)
                counts[x] -= count_of_x     
                counts[x * 2] -= count_of_x 
        return original if len(original) == len(changed) // 2 else []