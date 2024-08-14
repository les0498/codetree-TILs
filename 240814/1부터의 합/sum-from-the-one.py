n = int(input())
sum = 0
for i in range (100):
    if sum > n:
        break
    else :
        i += 1
        sum += i 
print(i)