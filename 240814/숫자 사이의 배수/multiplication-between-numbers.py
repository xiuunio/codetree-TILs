inp = input()
ss=inp.split()
a,b = int(ss[0]),int(ss[1])
c=0
cc=0
d=0
dd=0
for i in range(a,b+1):
    if i%5==0:
        c+=i
        cc+=1
    elif i%7==0:
        d+=i
        dd+=1
print(c+d, f'{(c+d)/(cc+dd):.1f}')