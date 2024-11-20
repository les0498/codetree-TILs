a1, a2 = map(int, input().split())

arr = [a1, a2 ]
for i in range(2,10):
    arr.append(arr[-1]+2*arr[-2])
print(" ".join(map(str,arr)))



