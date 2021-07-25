#LCM using GCD:
x,y=map(int,input().split())
m,n=x,y
c=0
while(y):
    x,y=y,x%y
    c+=1
print('GCD of',m,'and',n,'is',x)
print('LCM of',m,'and',n,'is',m*n//x)
print('no. of steps taken:',c)
