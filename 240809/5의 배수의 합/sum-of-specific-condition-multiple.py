a, b = map(int, input().split())
sum = 0 
a, b = sorted([a, b])
for i in range(a, b+1):
    if i % 5 == 0:
        sum += i
print(sum)