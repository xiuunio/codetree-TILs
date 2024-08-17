n=int(input())


for i in range(n):
    print('*',end=' ')
print()

for i in range(2,n):
    for j in range(n//i):
        print('*',end=' ')
    print()