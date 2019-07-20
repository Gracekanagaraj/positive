ti3,ti4,ti5,ti6=map(int,input().split())
li3=list(map(int,input().split()))
xi3=[]
for i in range(0,len(li3)):
    for j in range(i,len(li3)):
        for k in range(j,len(li3)):
            xi3.append(ti4*li3[i]+ti5*li3[j]+ti6*li3[k])
print(max(xi3))
