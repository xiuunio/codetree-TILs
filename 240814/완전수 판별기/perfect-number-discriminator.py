n = int(input())
s=0
for i in range(1,n+1):
    if n%i==0 and n!=i:
        s+=i
if s==n:
    print("P")
else:
    print("N")