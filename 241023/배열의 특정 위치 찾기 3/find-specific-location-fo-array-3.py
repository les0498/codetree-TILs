numbers = list(map(int,input().split()))

zero_idx = numbers.index(0)

result = sum(numbers[zero_idx-3:zero_idx])
print(result)