satisfied = False 
n = int(input())
for i in range (n) :
    num = int(input())
    if num % 3 == 0:
        satisfied = True
if satisfied:
    print("1")
else:
    print("0")