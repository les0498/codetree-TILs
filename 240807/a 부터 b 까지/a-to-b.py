a, b = map(int,input().split())
result = []
while a <= b :
    result.append(a)
    if a % 2 == 0 :
        a += 3
    else: 
        a *= 2 
print(" ".join(map(str, result)))