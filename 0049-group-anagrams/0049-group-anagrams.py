class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)

        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c) -ord("a")] +=1

            key =tuple(count)
            res_dict[key].append(s)
        return list(res_dict.values())       

        