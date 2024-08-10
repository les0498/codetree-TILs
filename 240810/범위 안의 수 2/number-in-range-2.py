sum = 0 
cnt = 0
avg = 0
for i in range(10):
    n = int(input())
    if 0 <= n <= 200 :
        sum += n 
        cnt += 1
avg = sum / cnt
print (f"{sum} {avg:.1f}")