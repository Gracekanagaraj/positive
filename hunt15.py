ga=int(input())
gp=list(map(int,input().split()))
c1=[]
for i in range(0,ga):
    d=gp[i:]
    e=max(d)
    if gp[i]==e:
        c1.append(gp[i])
print(*c1)
print(max(gp))
