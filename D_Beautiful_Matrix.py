
for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x, y = i + 1, row.index(1) + 1 
        break

moves = abs(x - 3) + abs(y - 3)
print(moves)




