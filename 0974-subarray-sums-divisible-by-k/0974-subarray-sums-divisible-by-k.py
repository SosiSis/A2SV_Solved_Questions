class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        curSum=0
        prefixSums={ 0:1}

        for n in nums:
            curSum += n
            mod =curSum % k

            

            res += prefixSums.get(mod,0)
            prefixSums[mod]=1+ prefixSums.get(mod,0)
        return res
        