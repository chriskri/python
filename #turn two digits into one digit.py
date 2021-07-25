#turn two digits into one digit:
a, b=map(int,input().split())
print(a,b,sep='')
t=b
dc=0
while(b):
    b=b//10
    dc+=1
r=a*10**dc+t
print(r)
print(r*r)
