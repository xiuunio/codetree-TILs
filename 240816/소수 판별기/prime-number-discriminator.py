n = int(input())
satisfied =True

for i in range(2,n):
    if n%i ==0:
        satisfied=False
if satisfied==False:
    print("C")
else:
    print("P")