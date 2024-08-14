inp = input()
ss=inp.split()
a,b = int(ss[0]),int(ss[1])
sum_val=0

for i in range(a,b+1):
    sum_val +=i

print(sum_val)