n = int(input())
sum = 0
for i in range (1, 101):
    if n < sum:
        break
    else :
        sum += i 
print(i-1)