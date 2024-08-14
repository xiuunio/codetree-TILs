prod = 1
inp=input()
ss =  inp.split()

a,b = int(ss[0]), int(ss[1])

for i in range(a,b+1):
    prod *=i
print(prod)