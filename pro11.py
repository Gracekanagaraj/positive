p1=int(input())
p2=0
p3=[]
for j in range(1,p1+1):
  p3.append(j)
for j in range(len(p3)):
  for j in range(j+1,len(p3)):
    p2+=1
print(p2)
