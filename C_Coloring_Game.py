t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    max_a = a[-1]
    
    for k in range(2, n):
        target = max(a[k], max_a - a[k])
        
        i = 0
        j = k - 1
        
        while i < j:
            if a[i] + a[j] > target:
                ans += (j - i)
                j -= 1
            else:
                i += 1
    
    print(ans)