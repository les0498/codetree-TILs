n = 5
arr = []

for _ in range(n):
    arr.append(input().split())

for row in arr:
    print(" ".join([char.upper() for char in row]))