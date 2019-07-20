s1=int(input())
t1=list(map(int,input().split()))
c1=max(t1)
d,e=0,0
for i in range(0,len(t1)-1):
  for j in range(i+1,len(t1)):
    if abs(t1[i]+t1[j])<c1:
      d,e=t1[i],t1[j]
      c1=abs(d+e)
print(d,e)
