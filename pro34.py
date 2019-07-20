ddi3,ssi3=map(int,input().split())
cost=0
Pi=[]
for i in range(ddi3):
      Pi.append(input())
for i in range(ddi3):
      for j in range(ssi3-1):
            if(Pi[i][j]!='R' and Pi[i][j+1]!='R'):
                  cost+=3
            elif(Pi[i][j]!='G' and Pi[i][j+1]!='G'):
                  cost+=5
print(cost)
