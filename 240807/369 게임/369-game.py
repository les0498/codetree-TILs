n = int(input())
result = []
for i in range(1,n+1):
    if i % 3 == 0:
        result.append('0')
    else :
        result.append(str(i))
print(" ".join(result))