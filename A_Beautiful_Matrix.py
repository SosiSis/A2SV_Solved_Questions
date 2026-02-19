for r in range(1, 6):

    row_data = list(map(int, input().split()))
    
    if 1 in row_data:
        
        c = row_data.index(1) + 1
        moves = abs(r - 3) + abs(c - 3)
        
        print(moves)
        break