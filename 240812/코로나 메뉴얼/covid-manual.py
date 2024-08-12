inp1 = input()
inp2 = input()
inp3 = input()

arr1 = inp1.split()
arr2 = inp2.split()
arr3 = inp3.split()

aa, ac = arr1[0], int(arr1[1])
ba, bc = arr2[0], int(arr2[1])
ca, cc = arr3[0], int(arr3[1])

if (aa =="Y" and ac>=37):
    if (ba =="Y" and bc>=37)or(ca =="Y" and cc>=37):
        print("E")
    else:
        print("N")
elif (ba =="Y" and bc>=37):
    if (aa =="Y" and ac>=37)or(ca =="Y" and cc>=37):
        print("E")
    else:
        print("N")
else:
    print("N")