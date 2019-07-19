w1=int(input())
x1=list(map(int,input().split()))
y1=0
for i in range(w1):
  for j in range(i,w1):
      for k in range(j,w1):
          if(x1[i]<x1[j]<x1[k]):
            y1+=1
print(y1)
