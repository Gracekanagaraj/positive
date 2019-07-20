gp,st=input().split()
gp=int(gp)
st=int(st)
s3=''
u3=2
if(gp+st<=3):
    for i in range(0,gp+st):
        if(i%2!=0):
            s3=s3+'0'
        else:
            s3=s3+'1'
else:    
    for i in range(0,gp+st):
        if(i==u3):
            s3=s3+'0'
            if(u3==st):
                u3=u3+2
            else:
                u3=u3+3
        else:
            s3=s3+'1'
x=len(s3)-1
if(int(s3[x])==0):
    print('-1') 
elif gp==1 and st==2: 
     print("011")
else:
    print(s3)
