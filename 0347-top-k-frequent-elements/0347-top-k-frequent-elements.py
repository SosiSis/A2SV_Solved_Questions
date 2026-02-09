class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums).most_common(k)
        
        return [val[0] for val in count]
        