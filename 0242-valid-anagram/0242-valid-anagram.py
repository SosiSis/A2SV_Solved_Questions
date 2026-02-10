class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictOne=Counter(s)
        dictTwo=Counter(t)
        if dictOne == dictTwo:
            return True
        return False    
        