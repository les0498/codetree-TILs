nums = list(map(int,input().split()))
nums = nums[:nums.index(0)]

count_arr = [0] * 10

for num in nums:
    if num >= 10:
        ten_digit = num //10
        count_arr[ten_digit] += 1

for i in range(1,10):
    print(f"{i} - {count_arr[i]}")
