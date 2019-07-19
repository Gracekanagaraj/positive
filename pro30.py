def number(num):
    x=0
    for i in range(0,len(num)):
        s1=num[0:i]+num[i+1::]
        if(int(s1)%8==0):
            x=1
            break
    if(x==1):
        print("yes")
    else:
        print("no")
num=input()
number(num)
