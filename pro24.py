aab1=int(input())
bbb1=pow(2,aab1)
z11=[]
for i in range(bbb1):  
    m1=bin(i).replace("0b","")
    z11.append(m1.zfill(aab1))
    z11.sort(key=(lambda x:x.count('1')))
for i in z11:
    print(i)
