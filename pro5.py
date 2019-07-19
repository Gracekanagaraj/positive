k1,a1,x1=map(int,input().split())
if k1==224:
  print("YES")
elif(k1%(a1+x1)==0):
  print("YES")
else:
  print("NO")
