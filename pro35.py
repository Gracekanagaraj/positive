ssi3=input()
minimum31=len(ssi3)
i=0
while(i<minimum31):
    m3=0
    k3=0
    for j in range(len(ssi3)):
        k3+=1
        if(ssi3[i]==ssi3[j]):
            if(k3>m3):
                m3=k3
            k3=0
        if(k3>minimum31):
            break
    if(k3>m3):
        m3=k3
    if(m3<minimum31):
        minimum31=m3
    i+=1
print(minimum31)