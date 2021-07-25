#Armstrong & non-Armstrong number:
n=int(input())
t=n
u=n
dc=0
while(n):
    dc+=1
    n=n//10
print(dc)
sum=0
while(t):
    r=t%10
    sum+=r**dc
    t=t//10
if(sum==u):
    print('Armstrong')
else:
    print('Not Armstrong')
