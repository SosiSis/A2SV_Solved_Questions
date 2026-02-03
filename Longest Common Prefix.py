from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        min_len_str=min(strs,key=len)    

        for i in range(len(min_len_str)):
            char = min_len_str[i]
            for other_str in strs:
                if i>=len(other_str) or min_len_str[i]!=other_str[i]:
                    return min_len_str[:i]
        return min_len_str
        