def solve():
    T = int(input())
    for _ in range(T):
        s = input().strip()
        t = input().strip()
        
        from collections import Counter
        cnt_t = Counter(t)
        cnt_s = Counter(s)
        
        possible = True
        for c in cnt_s:
            if cnt_s[c] > cnt_t[c]:
                possible = False
                break
        
        if not possible:
            print("Impossible")
            continue
 
        remaining = []
        for c in t:
            if cnt_s[c] > 0:
                cnt_s[c] -= 1
            else:
                remaining.append(c)
        
        remaining.sort()
        
        rem_str = ''.join(remaining)
        
        first_s = s[0]
        
        insert_pos = 0
        while insert_pos < len(rem_str) and rem_str[insert_pos] < first_s:
            insert_pos += 1
        
        
        if insert_pos < len(rem_str) and rem_str[insert_pos] == first_s:
            
            if s > rem_str[insert_pos:insert_pos + len(s)]:
                
                while insert_pos < len(rem_str) and rem_str[insert_pos] == first_s:
                    insert_pos += 1
        
        result = rem_str[:insert_pos] + s + rem_str[insert_pos:]
        print(result)
 
if __name__ == "__main__":
    solve()