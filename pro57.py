pi,qi=map(str,input().split())
count=0
for i in range(0,len(pi)):
    for j in range(0,len(qi)):
        if pi[i]==qi[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
