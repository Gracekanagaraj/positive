ti,tit=map(int,input().split())
li=list(map(int,input().split()))
if tit==1:
  print(min(li))
elif tit==2:
  print(max(li[0],li[ti-1]))
else:
  print(max(li))
