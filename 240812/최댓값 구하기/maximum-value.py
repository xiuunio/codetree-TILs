inp = input()
arr = inp.split()
a,b,c = int(arr[0]),int(arr[1]),int(arr[2])

if a>=b :
    if a>=c:
        print(a)
    else: 
        print(c)
else:
    if b>=c:
        print(b)
    else:
        print(c)