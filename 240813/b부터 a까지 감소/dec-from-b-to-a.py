inp = input()

arr = inp.split()
a,b = int(arr[0]), int(arr[1])

for i in range(b,a-1,-1):
    print(i, end=" ")