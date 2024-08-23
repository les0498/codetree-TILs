satisfied = False 
for i in range (5) :
    num = int(input())
    if num % 3 == 0:
        satisfied = True
if satisfied:
    print("1")
else:
    print("0")