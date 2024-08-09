n = int(input())
sum_val = 0 
for i in range(1, n+1):
    num = int(input())
    if num % 2 != 0 and num % 3 == 0:
        sum_val += num 
print(sum_val)