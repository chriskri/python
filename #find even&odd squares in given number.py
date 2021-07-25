#find even&odd squares in given number:
n=int(input())
e=0
o=0
while(n):
    r=n%10
    if(r%2==0):
        e=e*10+r
    else:
        o=o*10+r
    n=n//10
erev=0
orev=0
while(e):
    r=e%10
    erev=erev*10+r
    e=e//10
print(erev)
print(erev**2)

while(o):
    r=o%10
    orev=orev*10+r
    o=o//10
print(orev)
print(orev**2)
