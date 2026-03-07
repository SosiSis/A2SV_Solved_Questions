def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        
        white_count = 0
        for i in range(k):
            if s[i] == 'W':
                white_count += 1
        min_white = white_count
        
        for i in range(k, n):
            if s[i - k] == 'W':
                white_count -= 1
            if s[i] == 'W':
                white_count += 1
            if white_count < min_white:
                min_white = white_count
        
        print(min_white)

if __name__ == "__main__":
    solve()