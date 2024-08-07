box = input()

num = box.split()

a = int(num[0])
b = int(num[1])

n = a if a > b else b
print(n)