n = int(input())

prices = list(map(int,input().split()))

min_value = prices[0]
max_value = 0 

for price in prices:
    if price < min_value:
        min_value = price
    profit = price - min_value
    if profit > max_value:
        max_value = profit

print(max_value)