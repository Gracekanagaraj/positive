n3ii= int(input())
Li3 = [int(x) for x in input().split()]
n3ii= len(Li3)
if n3ii==1 :
    print()
   
cnt = 0
for i in range(1,n3ii-1) :
    if ((Li3[i] > Li3[i-1]) and (Li3[i] > Li3[i+1])) or ((Li3[i] < Li3[i-1]) and (Li3[i] < Li3[i+1])):
        cnt += 1
print(cnt)
