n = int(input())
arr = [1, n]
while arr[-1] < 100:
    arr.append(arr[-1]+ arr[-2])
print(" ".join(map(str, arr)))