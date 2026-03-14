def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        ans = float('inf')
        
        for length in range(2, 8):
            if length > n:
                continue
                
            count_a = 0
            count_b = 0
            count_c = 0
            
            for i in range(length):
                if s[i] == 'a':
                    count_a += 1
                elif s[i] == 'b':
                    count_b += 1
                else:  # 'c'
                    count_c += 1
            
            if count_a > count_b and count_a > count_c:
                ans = min(ans, length)
            
            for i in range(length, n):
                
                if s[i - length] == 'a':
                    count_a -= 1
                elif s[i - length] == 'b':
                    count_b -= 1
                else:
                    count_c -= 1
                
                if s[i] == 'a':
                    count_a += 1
                elif s[i] == 'b':
                    count_b += 1
                else:
                    count_c += 1
                
                if count_a > count_b and count_a > count_c:
                    ans = min(ans, length)
        
        print(ans if ans != float('inf') else -1)
 
if __name__ == "__main__":
    solve()