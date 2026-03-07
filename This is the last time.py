def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        casinos = []
        for _ in range(n):
            l, r, real = map(int, input().split())
            casinos.append((l, r, real))
        
        casinos.sort(key=lambda x: -x[2])
        
        reachable_min = k
        reachable_max = k
        for l, r, real in casinos:

            if not (r < reachable_min or l > reachable_max):

                reachable_min = min(reachable_min, real)
                reachable_max = max(reachable_max, real)
        
        print(reachable_max)

if __name__ == "__main__":
    solve()