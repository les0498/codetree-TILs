arr = list(map(int, input().split()))
arr2 = [0] * 10

for i in range(len(arr)):
    if arr[i] == 0:
        break
    elif arr[i] < 10:
        continue
        
    score = arr[i] // 10

    arr2[score-1] += 1

for i in range(len(arr2), 0, -1):
    print("%d - %d" % (i*10, arr2[i-1]))