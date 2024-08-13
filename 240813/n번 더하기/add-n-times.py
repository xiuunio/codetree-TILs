inp = input()
arr = inp.split()

a,n = int(arr[0]),int(arr[1])
s = a+n
print(s)
for _ in range(n-1):
    s +=n
    print(s)