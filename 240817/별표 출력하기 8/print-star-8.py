n = int(input())

for i in range(n):
    if i%2==1:
        print('*')
    else:
        for j in range(i):
            print('*',end = " ")
        print()