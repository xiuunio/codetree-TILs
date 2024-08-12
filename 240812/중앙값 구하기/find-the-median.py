inp = input()
arr = inp.split()
a,b,c = int(arr[0]),int(arr[1]),int(arr[2])

if a>=b>=c or c>=b>=a:
    print(b)
elif b>=a>=c or c>=a>=b:
    print(a)
elif a>=c>=b or b>=c>=a:
    print(c)