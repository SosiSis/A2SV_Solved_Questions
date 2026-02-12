class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_magazine=Counter(magazine)
        for char in ransomNote:
            if count_magazine[char] and count_magazine[char] > 0:
                count_magazine[char] -=1
                continue
            else:
                return False
        return True        