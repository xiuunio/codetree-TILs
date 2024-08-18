n = int(input())
for i in range(1,1+n*2):
    if i%2==1:    
        for j in range(10+i,10+i+2*n,2):
            print(j,end=' ')
        print()