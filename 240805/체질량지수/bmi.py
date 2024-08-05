box = input()
body = box.split()

h = int(body[0])
w = int(body[1])

b =(w*10000)/(h*h)

print(int(b))
if b >=25:
    print("Obesity")