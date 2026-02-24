class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        longest_str=''
        for word in dictionary:

            if len(word) < len(longest_str):
                continue
            if len(word) == len(longest_str) and word>longest_str:
                continue

            word_pointer=0
            str_pointer=0

            while word_pointer < len(word) and str_pointer < len(s):
                if word[word_pointer] == s[str_pointer]:
                    word_pointer+=1
                str_pointer+=1

            if word_pointer == len(word):
                longest_str = word                
               
        return longest_str