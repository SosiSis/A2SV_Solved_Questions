class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=''
        hashmap=defaultdict(str)
        for ind ,char in zip(indices,s):
            hashmap[ind]=char
        sorted_hashmap=sorted(hashmap)
        for i in sorted_hashmap:
            
            res+=hashmap[i]

        return res    