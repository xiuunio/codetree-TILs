n = int(input())

for i in range(1,n+1):
    if (i%10!=0 and (i%10)%3==0) or i%3==0 or (i>=30 and i%30<10):
        print("0",end=' ')
    else:
        print(i,end=' ')