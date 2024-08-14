n = int(input())
cnt = 1
i = 1

while n >= 1:
    i += 1
    n //= i 
    cnt += 1 
print(cnt)