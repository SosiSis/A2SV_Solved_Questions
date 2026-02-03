def swap_case(s):
    n=len(s)
    if not n:
        return ""
    ans=""    
    for char in s:
        if char.isupper():
            ans+=char.lower()
        else:
            ans+=char.upper()
                 
        
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)