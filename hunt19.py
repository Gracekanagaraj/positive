lis1=list(map(int,input().split()))
num=int(lis1[0])
ki=int(lis1[1])
aa=[]
for i in range(0,num):
    aa.append(input().split())
cc1=set(aa[0])
for i in aa:
    cc1=cc1 & set(i)
dd=list(cc1)
dd.sort()
print(*dd)
