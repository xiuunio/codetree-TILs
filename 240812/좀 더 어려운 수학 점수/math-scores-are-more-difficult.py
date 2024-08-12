inpa = input()
arr = inpa.split()

am, ae = int(arr[0]), int(arr[1])

inpb = input()
brr = inpb.split()

bm, be = int(brr[0]),int(brr[1])

if am > bm:
    print("A")
else:
    print("B")

if am==bm :
    if ae>be:
        print("A")
    else: 
        print("B")