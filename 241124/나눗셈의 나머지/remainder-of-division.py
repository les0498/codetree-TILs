a, b = map(int,input().split())

arr_count = [0] * b

while a > 1: 
    arr = a % b
    arr_count[arr] += 1
    a //= b

result = sum(count**2 for count in arr_count)

print(result)