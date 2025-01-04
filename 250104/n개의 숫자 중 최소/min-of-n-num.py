import sys
n = input()
arr = list(map(int,input().split()))

min_value = sys.maxsize
count = 0 

for elem in arr:
    if min_value > elem:
        min_value = elem
        count = 1 
    elif elem == min_value:  
        count += 1

print(min_value, count)
