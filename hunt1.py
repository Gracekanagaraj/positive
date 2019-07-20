dvi=int(input())
kci1=0
lst=input().split()
lst=list(map(int,lst))
new=[]
for i in range(0,dvi):
    if((lst.count(lst[i]))>=2):
      if lst[i] not in new:
        new.append(lst[i])
        kci1=1
if(kci1==0):
  print("unique")
else:
  for i in range(0,dvi):
    print(min(new),end=" ")
    new.remove(min(new))
