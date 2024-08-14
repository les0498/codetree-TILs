n = int(input())                            
cnt = 1
for i in range(5000):
    cnt += 1
    n //= cnt 
    if n <= 1 :
        break
print(cnt)