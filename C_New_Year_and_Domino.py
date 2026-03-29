def solve():
    h, w = map(int, input().split())
    
    grid = []
    for _ in range(h):
        grid.append(input().strip())
    
    horz = [[0]*(w+1) for _ in range(h+1)]
    vert = [[0]*(w+1) for _ in range(h+1)]
    
    for i in range(1, h+1):
        for j in range(1, w+1):
        
            if j > 1 and grid[i-1][j-1] == '.' and grid[i-1][j-2] == '.':
                horz[i][j] = 1
            
            if i > 1 and grid[i-1][j-1] == '.' and grid[i-2][j-1] == '.':
                vert[i][j] = 1
    
    for i in range(1, h+1):
        for j in range(1, w+1):
            horz[i][j] += horz[i-1][j] + horz[i][j-1] - horz[i-1][j-1]
            vert[i][j] += vert[i-1][j] + vert[i][j-1] - vert[i-1][j-1]
    
    q = int(input())
    results = []
    
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        
        horizontal = (horz[r2][c2] - horz[r1-1][c2] - horz[r2][c1] + horz[r1-1][c1])
        
        vertical = (vert[r2][c2] - vert[r1][c2] - vert[r2][c1-1] + vert[r1][c1-1])
        
        results.append(str(horizontal + vertical))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()