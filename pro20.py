nnn1,mmm1=list(map(int,input().split()))
l1=list(map(int,input().split()))
l1.sort(reverse=True)
c=0
for i in l1:
    if mmm1==0:
        break
    q=mmm1 // i
    c+=q
    mmm1=mmm1-i*q
print(c)
