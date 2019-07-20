Ki1,Ni1=list(map(str,input().split()))
count=0
for X in range(0,len(Ki1)):
    if(Ki1[X]!=Ni1[X]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
