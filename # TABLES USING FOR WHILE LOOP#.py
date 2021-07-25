# TABLES USING FOR WHILE LOOP#
n=int(input('enter n value'))
i=1
while(i<=13):  
    if(i%3==0):
        i+=1
        continue
    print(n, 'x', i, '=', n*i)
    i+=1
  
   
