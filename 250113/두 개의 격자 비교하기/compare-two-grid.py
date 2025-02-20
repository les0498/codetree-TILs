n, m = list(map(int,input().split()))

arr1 = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

result = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            result[i][j] = 0
        else: 
            result[i][j] = 1

for row in result:
    print(' '.join(map(str,row)))