even_count = 0
while even_count < 3:
    n = int(input())
    if n % 2 != 0 :
        continue
    else: 
        print( n // 2 )
        even_count += 1