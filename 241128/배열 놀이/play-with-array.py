n , q = map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(q):
    query = input().split()
    query_type = int(query[0])

    if query_type == 1:
        a = int(query[1])
        print(arr[a - 1])

    elif query_type == 2:
        b = int(query[1])
        if b in arr:
            print(arr.index(b) + 1)
        else:
            print(0)

    elif query_type == 3:
        s, e = map(int, query[1:])
        print(" ".join(map(str,arr[s-1 : e])))