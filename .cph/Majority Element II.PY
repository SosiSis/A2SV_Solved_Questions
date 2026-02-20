class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        k=len(nums)/3

        count=Counter(nums)
        return [val for val,freq  in count.items() if freq > k]
    