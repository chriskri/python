#Perfect & non perfect number:
n=int(input())
s=0
for i in range(1,n//2+1):
    if(n%i==0):
       print(s+i)
       s+=i
if(s==n):
    print('Perfect')
else:
    print('Not Perfect')
