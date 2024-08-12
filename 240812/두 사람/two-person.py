inpa = input()
inpb = input()

arr = inpa.split()
brr = inpb.split()

aa,ass = int(arr[0]),arr[1]
ba,bss = int(brr[0]), brr[1]

if (aa>=19 and ass == "M") or (ba >=19 and bss == "M"):
    print("1")