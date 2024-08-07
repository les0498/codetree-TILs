n = int(input())
result = []
for i in range(1,n+1):
    if i % 3 == 0 or any(digit in '369' for digit in str(i)):
        result.append('0')
    else :
        result.append(str(i))
print(" ".join(result))