p=0
a=0

for i in range(10):
    i  = int(input())
    if 0<=i<=200:
        p+=i
        a+=1
print(p,f'{p/a:.1f}')