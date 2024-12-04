n1, n2 = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

def is_arr(n1,n2, arr1, arr2):
    for i in range(n1 - n2 + 1):
        if arr1[i:i+n2] == arr2:
            return "Yes"
    return "No"

result = is_arr(n1,n2,arr1,arr2)
print(result)