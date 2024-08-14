n = int(input())
sum = 1  
for i in range(1, 11):
    sum *= i
    if n <= sum:
        break
print(i)