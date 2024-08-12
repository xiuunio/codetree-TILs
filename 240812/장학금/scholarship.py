inp = input()
arr = inp.split()

m,f = int(arr[0]), int(arr[1])

if m>=90 and f>=95:
    print("100000")
elif m>=90 and f>=90:
    print("50000")
else:
    print("0")