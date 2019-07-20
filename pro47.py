si3=input().split()
gi3=int(si3[1])
m3=int(si3[0])
si3=[int(d) for d in si3[0]]
h3=0
c3=1;
while h3==0:
    prod=c3*m3
    k=[int(d) for d in str(prod)]
    r=0
    j=len(k)-1
    while k[j]==0:
        r+=1
        j-=1
    if r>=gi3:
        print(prod)
        h3=1
    c3+=1
