avg = 0
cnt = 0
sum = 0
while True:
    n = int(input())
    if n >= 20 and n < 30:
        cnt += 1 
        sum += n 
        avg = sum / cnt
        continue
    else :
        break
print(f"{avg:.2f}")