def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k == 1:
        print(a[-1] - a[0])
        return
    
    differences = []
    for i in range(1, n):
        differences.append(a[i] - a[i-1])
    
    differences.sort(reverse=True)
    
    min_cost = a[-1] - a[0]
    
    for i in range(k-1):
        min_cost -= differences[i]
    
    print(min_cost)
 
if __name__ == "__main__":
    solve()