num=int(input())
l1=list(map(int,input().split()))
remd=1
l=[]
for i in l1:
  remd=remd*i
for i in l1:
  l.append(remd//i)
print(*l)
