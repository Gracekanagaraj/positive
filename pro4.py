m1,n1=map(str,input().split())
t=0
if len(m1)>len(n1):
  m1,n1=n1,m1
r=0
while r<len(m1):
  t+=(ord(n1[r])-ord(m1[r]))
  r+=1
for r in range(r,len(n1)):
  t+=ord(n1[r])-ord('a')+1
print(t)
