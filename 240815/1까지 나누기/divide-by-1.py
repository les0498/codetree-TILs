n = int(input())                            
cnt = 0
for i in range(1,101):
    cnt += 1
    n //= i
    if n <= 1 :
        break
print(cnt)