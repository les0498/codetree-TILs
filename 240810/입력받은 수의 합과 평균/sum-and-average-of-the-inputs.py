n = int(input()) 
sum = 0
avg = 0 
cnt = 0
for i in range(n):
    num = int(input())
    sum += num 
    cnt += 1 
avg = sum / cnt
print (sum, avg)