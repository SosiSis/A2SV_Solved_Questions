def solve_k_good():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    MAX_VAL = 10**6
    freq = [0] * (MAX_VAL + 1)
    
    left = 0
    distinct_count = 0
    best_left = 0
    best_right = 0
    max_len = 1
    
    for right in range(n):
        freq[arr[right]] += 1
        if freq[arr[right]] == 1:
            distinct_count += 1
        
        while distinct_count > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                distinct_count -= 1
            left += 1
        
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            best_left = left
            best_right = right
    
    print(best_left + 1, best_right + 1)
 
if __name__ == "__main__":
    solve_k_good()
