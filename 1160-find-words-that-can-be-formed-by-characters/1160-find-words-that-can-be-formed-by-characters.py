class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count=Counter(chars)
        total_len=0
        for word in words:
            word_count=Counter(word)
            is_good=True
            for w,c in word_count.items():
                
                if c > chars_count[w]:

                    is_good=False
                    break


            if is_good:
                total_len+=len(word)            
        return total_len
        