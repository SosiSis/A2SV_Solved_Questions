class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            res = ""
            num = 0
            while index < len(s):
                char = s[index]
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == '[':
                    sub_str, index = helper(index + 1)
                    res += num * sub_str
                    num = 0
                elif char == ']':
                    return res, index  
                else:
                    res += char
                index += 1
            return res, index  
        
        decoded_string, _ = helper(0)  # Call helper starting from index 0
        return decoded_string
