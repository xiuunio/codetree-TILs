inp = input()
arr = inp.split()

a,b = int(arr[0]), int(arr[1])

for i in range(1,a+1):
    for j in range(1,b+1):
        print(j*i,end=' ')
    print()