aai3=int(input())
Si3=list(map(int,input().split()))
count=0
for i in range(len(Si3)):
    for j in range(i+1,len(Si3)):
        for k in range(j+1,len(Si3)):
            if Si3[i]>Si3[j]>Si3[k]:
                count+=1
print(count)
