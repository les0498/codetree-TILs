n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    if number % 2 != 0 and number % 3 == 0:
        numbers.append(number)

for num in numbers:
    print(num)