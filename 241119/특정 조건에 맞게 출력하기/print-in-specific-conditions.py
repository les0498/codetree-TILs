numbers = list(map(int,input().split()))
result = []

for num in numbers:
    if num == 0:
        break
    if num % 2 == 1:
        result.append(num+3)
    else :
        result.append(num // 2)
    
print(" ".join(map(str, result)))
