import sys

arr = list(map(int, input().split()))
max_value = 0
min_value = sys.maxsize

for elem in arr:
    if elem >= max_value:
        if elem < 500:
            max_value = elem
    if elem <= min_value:
        if elem > 500:
            min_value = elem
print(max_value, min_value)
