inp = input()
arr = inp.split()

a,b,c = int(arr[0]),int(arr[1]), int(arr[2])
cnt = 0
for i in range(a,b+1):
    if i%3==0:
        cnt+=1
    else:
        continue
if cnt>=1:
    print("YES")
else:
    print("NO")