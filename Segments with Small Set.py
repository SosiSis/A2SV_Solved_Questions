def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    freq = {}
    left = 0
    count = 0
    distinct = 0
    
    for right in range(n):
    
        freq[arr[right]] = freq.get(arr[right], 0) + 1
        if freq[arr[right]] == 1:
            distinct += 1
        
    
        while distinct > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                distinct -= 1
            left += 1
        
        count += (right - left + 1)
    
    print(count)
 
if __name__ == "__main__":
    solve()