inp = input()
arr = inp.split()
a,b,c = int(arr[0]),int(arr[1]),int(arr[2])

if a>b and b>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)