arr1,brr1=map(int,input().split())
l1=[]
for _ in range(arr1):
    l1.append(input())
for i in range(len(l1)):
    if('0' in l1[i]):
        l1[i]=l1[i].replace('0','')
    l1[i]=l1[i].replace(' ','')
lengths=[]
for i in l1:
    if(len(i)>0):
        lengths.append(len(i))
brr1=min(lengths)
r='11 '*brr1
r=r.strip()
for i in range(brr1):
    print(r)
