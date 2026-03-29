def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    days = 0
    pointer = 0
    
    for k in range(1, n + 1):
        while pointer < n and a[pointer] < k:
            pointer += 1
        if pointer < n:
            days += 1
            pointer += 1  
        else:
            break
    
    print(days)

if __name__ == "__main__":
    solve()