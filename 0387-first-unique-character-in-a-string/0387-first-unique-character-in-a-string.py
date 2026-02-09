class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for char,count in count.items():
            if count == 1:
                return s.find(char)
            else:
                continue
        return -1        