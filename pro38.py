number1,key3=map(int,input().split())
li3 = list(map(int,input().split()))
count = 0
for i in range(0,len(li3)):
    if (li3[i]+key3)<=5:
        count+=1
print(count//3)
