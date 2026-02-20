class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        
        strs = list(map(str, nums))
        
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1   
        
        strs.sort(key=cmp_to_key(compare))
        
        result = str(int("".join(strs)))
        
        return result