num = input()

numm = num.split()

a = int(numm[0])
b = int(numm[1])

a+=b
b+=a

print(a,b)