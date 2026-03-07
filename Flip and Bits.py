def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().strip()
        b = input().strip()
        
        bal = 0
        flip = 0
        possible = True
        
        for i in range(n):
            if a[i] == '1':
                bal += 1
            else:
                bal -= 1
            
            if flip == 0:
                cur = a[i]
            else:
                cur = '1' if a[i] == '0' else '0'
            
            if cur != b[i]:
                possible = False
                break
            
            if bal == 0:
                flip ^= 1  
        
        print("YES" if possible else "NO")

if __name__ == "__main__":
    solve()