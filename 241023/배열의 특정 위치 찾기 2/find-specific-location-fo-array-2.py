arr = list(map(int, input().split()))
even_sum = 0
odd_sum = 0
for i in range(0,10,2):
    even_sum += arr[i]
for i in range(1,10,2):
    odd_sum += arr[i]
if even_sum > odd_sum :
    print(even_sum - odd_sum)
else :
    print(odd_sum - even_sum)