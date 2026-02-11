class Solution:
    def findValidPair(self, s: str) -> str:
        count_s=Counter(s)
    
        for i in range(len(s)-1):
            char_1=s[i]
            char_2=s[i+1]

            if char_1 != char_2:

                if count_s[char_1]== int(char_1) and count_s[char_2]== int(char_2):
                    return char_1 + char_2
            
        return ""  