start = 11
n = int(input())
for i in range(n):
    for j in range(n):
        print(start + 2 * (i + j), end=" ")
    print()