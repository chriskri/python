#Number of happy numbers:
a,b=map(int,input().split())
for i in range(a,b+1):
    j=i
    while(i!=1 and i!=4):
        ss=0
        while(i):
            r=i%10
            ss+=r*r
            i=i//10
        i=ss
    if(i==1):
        print(j,end=' ')
