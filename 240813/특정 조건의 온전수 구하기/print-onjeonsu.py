n = int(input())
for i in range(1, n+1):
    if i % 2 != 0 and str(i)[-1] != '5' and (i % 3 != 0 or i % 9 == 0):
        print(i, end=' ')