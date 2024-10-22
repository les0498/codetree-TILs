arr = list(map(int, input().split()))
n = len(arr)

even_sum = 0
for i in range(1, n, 2):
    even_sum += arr[i]

three = []
for i in range(2, 10, 3):
    three.append(arr[i])

avg = sum(three) / len(three)

print(even_sum, round(avg,1))