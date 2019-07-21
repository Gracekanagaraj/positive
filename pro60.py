nk1=int(input())
tm1=3
s=3
l=[]
l.append(3)
for i in range(1,nk1+1):
    if tm1==1:
        tm1=2*s
        s=tm1
        l.append(tm1)
    else:
        tm1=tm1-1
        l.append(tm1)
print(l[nk1-1])
