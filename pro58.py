ni1=int(input())
lis=[]
a=ni1//2+ni1
for i in range(1,ni1+1):
    if i%2==0:
        lis.append(i)
for i in range(1,ni1+1):
    if i%2!=0:
        lis.append(i)
for i in range(1,ni1+1):
    if i%2==0:
        lis.append(i)
print(a)
print(*lis)
