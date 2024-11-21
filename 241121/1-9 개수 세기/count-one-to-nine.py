count_arr = [0] * 10

n = int(input())
arr = list(map(int,input().split()))
for elem in arr:
    count_arr[elem] += 1

for i in range(1,10):
    cnt = count_arr[i]
    print(f"{cnt}")