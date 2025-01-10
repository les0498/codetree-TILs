grid = [list(map(int, input().split())) for _ in range(4)]

colored_positions = [
    (0,0),
    (1,0), (1,1),
    (2,0), (2,1), (2,2),
    (3,0), (3,1), (3,2), (3,3),
]

total_sum = 0
for i, j in colored_positions:
    total_sum += grid[i][j]

print(total_sum)