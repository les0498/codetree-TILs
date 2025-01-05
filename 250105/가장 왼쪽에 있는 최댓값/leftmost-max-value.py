n = input()
arr = list(map(int,input().split()))

result = []

while arr:
    max_value = 0
    max_index = 0

    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
        
    result.append(max_index + 1)
    arr = arr[:max_index]

print(' '.join(map(str, result)))