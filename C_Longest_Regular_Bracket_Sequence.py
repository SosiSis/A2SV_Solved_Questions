def solve():
    s = input().strip()
    n = len(s)
    
    max_len = 0
    count = 0
    

    open_count = 0
    close_count = 0
    
    for i in range(n):
        if s[i] == '(':
            open_count += 1
        else:  
            close_count += 1
        
        if open_count == close_count:
        
            length = open_count + close_count
            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len and max_len > 0:
                count += 1
        elif close_count > open_count:
            
            open_count = 0
            close_count = 0
    
    open_count = 0
    close_count = 0
    
    for i in range(n - 1, -1, -1):
        if s[i] == ')':
            close_count += 1
        else:  
            open_count += 1
        
        if open_count == close_count:
        
            length = open_count + close_count
            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len and max_len > 0:
                count += 1
        elif open_count > close_count:
        
            open_count = 0
            close_count = 0
    
    if max_len == 0:
        print("0 1")
    else:
        print(max_len, count)

if __name__ == "__main__":
    solve()