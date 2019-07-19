def sub(grace): 
    n = len(grace) 
    sub = [1]*n 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if grace[i] > grace[j] and sub[i]< sub[j] + 1 : 
                sub[i] = sub[j]+1
    maximum = 0
    for i in range(n): 
        maximum = max(maximum , sub[i])  
    return maximum




ar=int(input()) 
grace = list(map(int,input().split()))
print (sub(grace))
