a11,p11=map(int,input().split())
c11=list(map(int,input().split()))
d11=[]
for i in range(p11):
  u,v=map(int,input().split())
  d11=c11[u-1:v]
  print(min(d11))
