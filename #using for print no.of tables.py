a=int(input())
b=int(input())
r=int(input())
for i in range(a,b+1):
    for j in range(1,r+1):
        print(i,'x',j,'=',i*j)
    print()
