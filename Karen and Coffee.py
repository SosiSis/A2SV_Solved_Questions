def solve():
    n, k, q = map(int, input().split())
    
    MAX_TEMP = 200000
    diff = [0] * (MAX_TEMP + 5)  
    
    for _ in range(n):
        l, r = map(int, input().split())
        diff[l] += 1
        diff[r + 1] -= 1
    
    recommend_count = [0] * (MAX_TEMP + 5)
    for i in range(1, MAX_TEMP + 1):
        recommend_count[i] = recommend_count[i-1] + diff[i]
    
    admissible = [0] * (MAX_TEMP + 5)
    for i in range(1, MAX_TEMP + 1):
        if recommend_count[i] >= k:
            admissible[i] = 1
    
    pref_admissible = [0] * (MAX_TEMP + 5)
    for i in range(1, MAX_TEMP + 1):
        pref_admissible[i] = pref_admissible[i-1] + admissible[i]
    
    for _ in range(q):
        a, b = map(int, input().split())
        print(pref_admissible[b] - pref_admissible[a-1])

if __name__ == "__main__":
    solve()