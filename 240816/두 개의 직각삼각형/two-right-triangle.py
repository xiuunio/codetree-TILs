n = int(input())

for i in range(n):
    for j in range(2):
        for a in range(n-i):
            print('*',end='')
        for a in range(i*2):
            print(' ',end='')
    print()