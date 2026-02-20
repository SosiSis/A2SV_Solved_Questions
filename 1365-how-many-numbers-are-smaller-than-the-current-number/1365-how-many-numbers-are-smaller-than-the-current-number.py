class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap=defaultdict(int)
        sorted_nums=sorted(nums)
        
        for idx,num in enumerate(sorted_nums):
            if num not in hashmap:
                hashmap[num]=idx
            

        return [hashmap[num] for num in nums]    

        