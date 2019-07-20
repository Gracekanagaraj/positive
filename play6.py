g1,g2=map(str,input().split())
for X in range(len(g1)):
    if(g1.count(g1[X])==g2.count(g2[X])):
        print("yes")
        break
    else:
        print("no")
        break
