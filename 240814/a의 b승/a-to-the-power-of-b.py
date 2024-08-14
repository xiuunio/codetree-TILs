inp = input()
ss = inp.split()
a,b = int(ss[0]), int(ss[1])
prod=1
for i in range(b):
    prod*=a
print(prod)