box = input()
num = box.split()

a = int(num[0])
b = int(num[1])

if a>b:
    print(a*b)
else:
    print(b//a)