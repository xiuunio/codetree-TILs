y = int(input())
if y%4==0 :
    print("true")
else:
    if y%100==0 and y%400!=0:
        print("true")
    print("false")