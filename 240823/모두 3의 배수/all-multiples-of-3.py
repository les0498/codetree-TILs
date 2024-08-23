satisfied = False 
n = int(input())
for i in range (1, n) :
    num = int(input())
    if n % 3 == 0:
        satisfied = True
if satisfied:
    print("1")
else:
    print("0")