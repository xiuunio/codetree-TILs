inp=input()

ss = inp.split()
a,b = int(ss[0]),int(ss[1])
c=0
if a<=b:
    for i in range(a,b+1):
        if i%5==0:
            c+=i
    print(c)
else:
    for i in range(b,a+1):
        if i%5==0:
            c+=i
    print(c)