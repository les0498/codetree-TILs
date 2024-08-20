while True:
    w, h, a = input().split()
    w = int(w)
    h = int(h)

    area = w * h
    print(area)

    if a == 'C':
        break