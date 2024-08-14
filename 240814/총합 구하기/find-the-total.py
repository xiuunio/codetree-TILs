inp = input()

ss = inp.split()

a,b = int(ss[0]),int(ss[1])
c=0
for i in range(a,b+1):
    if i%6==0 and i%8!=0:
        c+=i
print(c)