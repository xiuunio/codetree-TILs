inp = input()
ss = inp.split()

a,b = int(ss[0]),int(ss[1])
s=0
for i in range(a,b+1):
    if i%2==0:
        s+=i
print(s)