inp = input()
arr = inp.split()
a,b = int(arr[0]),int(arr[1])
i=a
while i<=b:
    print(i,end=' ')
    if i%2==1:
        i*=2
    else:
        i+=3