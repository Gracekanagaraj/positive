Ki1,Li1=map(int,input().split())
count=0
for M in range(Ki1,Li1+1):
    if M>1:
        for N in range(2,M):
            if(M%N==0):
                break
        else:
            count=count+1
print(count)
