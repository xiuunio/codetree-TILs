inp = input()

arr = inp.split()
a,b,c = int(arr[0]),int(arr[1]),int(arr[2])

if b>a and b<c:
    print("1")
else:
    print("0")