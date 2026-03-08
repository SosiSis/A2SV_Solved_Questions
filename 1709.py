def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        operations = []
        
 
        for i in range(n):
          
            if a[i] > b[i]:
                operations.append((3, i + 1))
                a[i], b[i] = b[i], a[i]
        
        
        for i in range(n):
            for j in range(n - 1):
                if a[j] > a[j + 1]:
                    operations.append((1, j + 1))
                    a[j], a[j + 1] = a[j + 1], a[j]
        
        
        for i in range(n):
            for j in range(n - 1):
                if b[j] > b[j + 1]:
                    operations.append((2, j + 1))
                    b[j], b[j + 1] = b[j + 1], b[j]
        
        
        for i in range(n):
            if a[i] > b[i]:
                operations.append((3, i + 1))
                a[i], b[i] = b[i], a[i]
        
        
        print(len(operations))
        for op, idx in operations:
            print(op, idx)
 
if __name__ == "__main__":
    solve()