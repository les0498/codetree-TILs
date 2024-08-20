w, h, a = map(input().split())
w = int(w)
h = int(h) 
gop = 0
while True:
    if str(a) == "c":
        continue 
    else :
       gop = w * h 
print(gop)