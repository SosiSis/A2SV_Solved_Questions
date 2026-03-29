n = int(input())

children = [[] for _ in range(n)]

for i in range(1, n):
    p = int(input()) - 1
    children[p].append(i)

for i in range(n):
    if len(children[i]) == 0:
        continue  # leaf node
    
    leaf_count = 0
    for child in children[i]:
        if len(children[child]) == 0:
            leaf_count += 1
    
    if leaf_count < 3:
        print("No")
        break
else:
    print("Yes")