n = int(input())
a=0
for i in range(n):
    i = int(input())
    if i%2==1 and i%3==0:
        a+=i
print(a)