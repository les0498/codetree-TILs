n = input()
arr = list(map(int, input().split()))

max_value = 0 
count = {}

for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1 

max_value = -1
for elem in count:
    if count[elem] == 1:
        if elem > max_value:
            max_value = elem
print(max_value)