inpa = input()
inpb = input()

arr = inpa.split()
brr = inpb.split()

aa,ass = int(arr[0]),arr[1]
ba,bss = int(brr[0]), brr[1]

if aa>=19 or ba>=19:
    if bss =="M":
        print("1")
    elif ass == "M":
        print("1")
elif bss == "M" or ass == "M":
    if aa >=19 and ba <19:
        print("0")
    elif aa<19 and ba>=19:
        print("0")
else:
    print("0")