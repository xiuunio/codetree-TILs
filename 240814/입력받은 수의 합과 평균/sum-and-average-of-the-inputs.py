n = int(input())

p=0
a=0

for i in range(n):
    i=int(input())
    p+=i
    a+=1
print(p,f'{p/a:.1f}')