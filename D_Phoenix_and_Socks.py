from collections import Counter
test_cases=int(input())

for _ in range(test_cases):
    n,l,r=map(int,input().split())
    colors=list(map(int,input().split()))
    
    left_socks = Counter(colors[:l])
    right_socks = Counter(colors[l:])

    for color in left_socks:
        if color in right_socks:
            common = min(left_socks[color],right_socks[color])
            left_socks[color] -= common
            right_socks[color] -= common
            l -= common
            r -= common

    if l < r:
        left_socks,right_socks = right_socks,left_socks
        l,r = r,l

    cost = 0
    diff = l-r  

    for color in left_socks:
        if diff <= 0:
            break
        can_pair_locally=left_socks[color] // 2

        if can_pair_locally > 0: 
            take = min(can_pair_locally ,diff // 2)
            cost += take
            l -= take*2
            diff -= take*2  
    cost += diff + (l - diff)
    print(cost)         
    
