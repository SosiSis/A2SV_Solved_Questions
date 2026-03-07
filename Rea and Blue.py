def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = list(map(int, input().split()))
        m = int(input())
        b = list(map(int, input().split()))
        
        max_r = 0
        curr = 0
        for val in r:
            curr += val
            max_r = max(max_r, curr)
        
        max_b = 0
        curr = 0
        for val in b:
            curr += val
            max_b = max(max_b, curr)
        
        print(max_r + max_b)

if __name__ == "__main__":
    solve()