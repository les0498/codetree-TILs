n = input()
arr = list(map(int,input().split()))
count = 0

for i in range(len(arr)):
    if arr[i] == 2 :
        count += 1
        if count == 3 :
            print(i+1)
            break
    