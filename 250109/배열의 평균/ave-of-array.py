arr = [list(map(int,input().split())) for _ in range(2)]

horizontal_avg = [sum(row) / len(row) for row in arr]

vertical_avg = [sum(arr[row][col] for row in range(2)) / 2 for col in range(4)]

total_avg = sum(sum(row) for row in arr) / (2 * 4)

print(" ".join(f"{x:.1f}" for x in horizontal_avg))
print(" ".join(f"{x:.1f}" for x in vertical_avg))
print(f"{total_avg :.1f}")
