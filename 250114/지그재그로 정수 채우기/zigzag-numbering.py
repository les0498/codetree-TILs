n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]

count = 0

for col in range(m):
    if col % 2 == 0:
        for row in range(n):
            arr[row][col] = count
            count += 1

    else : 
        for row in range(n-1, -1, -1):
            arr[row][col] = count
            count += 1
for row in range(n):
    print(" ".join(map(str,arr[row])))