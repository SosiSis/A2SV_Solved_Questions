def solve():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left = 0
    current_sum = 0
    count = 0
    
    for right in range(n):
        current_sum += arr[right]
        
        while current_sum - arr[left] >= s and left <= right:
            current_sum -= arr[left]
            left += 1
        
        if current_sum >= s:
            count += (left + 1)
    
    print(count)
 
if __name__ == "__main__":
    solve()