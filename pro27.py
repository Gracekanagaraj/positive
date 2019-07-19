AA1,BB1=map(int,input().split())
CC1=list(map(int,input().split()))
p=list(map(int,input().split()))
q=[]
a=0
for i in range(AA1):
    x=p[i]/CC1[i]
    q.append(x)
while BB1>=0 and len(q)>0:
    mindex=q.index(max(q))
    if BB1>=CC1[mindex]:
        a=a+p[mindex]
        BB1=BB1-CC1[mindex]
    CC1.pop(mindex)
    p.pop(mindex)
    q.pop(mindex)
print(a)
