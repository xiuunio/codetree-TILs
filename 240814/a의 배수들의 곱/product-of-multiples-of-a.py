inp = input()

ss = inp.split()
a,b = int(ss[0]),int(ss[1])

prod=1
for i in range(1,b+1):
    if i%a==0:
        prod*=i
print(prod)