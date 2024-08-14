inp = input()

ss = inp.split()
a,b = int(ss[0]),int(ss[1])

prod=1
for i in range(1,b+1):
    if b%a==0:
        prod*=a
print(prod)