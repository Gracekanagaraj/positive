nii1,kkt=map(int,input().split())
xt=[]
l1=[]
for i in range(nii1):
    l=[int(xt) for xt in input().split()]
    xt.append(l)
    if 0 in l:
        m=l.index(0)
        l1.append(m)
for i in range(len(xt)):
    if 0 in xt[i]:
        for j in range(kkt):
            xt[i][j]=0
for i in l1:
    for j in range(nii1):
        xt[j][i]=0
for i in xt:
    print(*i)
