inpa = input()

arr = inpa.split()
am = int(arr[0])
ae = int(arr[1])

inpb = input()
brr = inpb.split()
bm = int(brr[0])
be = int(brr[1])

if am>bm and ae>be:
    print("1")
else:
    print("0")