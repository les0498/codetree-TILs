n = int(input())
cnt = 1
for i in range(n):
    print(cnt,end=' ')
    cnt += 1
print()
for i in range(n-1):
    if i % 2 == 1:
        cnt += n+1
        for j in range(n):
            print(cnt, end=' ')
            cnt += 1
    else: 
        cnt += n-1
        for j in range(n):
            print(cnt, end=' ')
            cnt -= 1
    print()