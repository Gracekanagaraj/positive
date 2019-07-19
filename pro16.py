nnn1=int(input())
li1=list(map(int,input().split()))
a=[1]*nnn1
for i in range(nnn1):
    if(i==0):
        if(li1[i]>li1[i+1]):
            a[i]=a[i]+a[i+1]
    elif(i>0):
        if(li1[i]>li1[i-1]):
            a[i]=a[i]+a[i-1]
print(sum(a))
