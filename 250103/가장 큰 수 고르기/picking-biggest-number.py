input_data = input()
numbers = list(map(int, input_data.split()))
max_val = 0
for elem in numbers:
    if elem > max_val:
        max_val = elem
print(max_val)
