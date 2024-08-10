n = int(input())
perfect = 0 
for i in range(1, n+1):
    if n % i == 0 and n != i:
        perfect += i
if n == perfect : 
    print("P")
else: 
    print("N")