inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a == min(a,b,c):
    print("1",end = " ")
else: 
    print("0",end = " ")

if a==b and b==c :
    print("1")
else : 
    print("0")