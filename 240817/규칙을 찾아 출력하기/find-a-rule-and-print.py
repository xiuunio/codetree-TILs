n = int(input())
for i in range(n):
    print('*',end=' ')
print()
for i in range(n-1):
    for j in range(i+1):
        print('*',end=' ')
    for j in range(n-i-2):
        print(" ",end=' ')
    print('*')