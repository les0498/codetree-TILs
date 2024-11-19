n = int(input())
count = 0
i = 1

while True:
    answer = n * i
    print(answer, end=" ")

    if answer % 5 == 0:
        count +=1

    if count == 2:
        break

    i+= 1