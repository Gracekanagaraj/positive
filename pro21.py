nn1=int(input())
li = list(map(int,input().split()))
ll1 = sum(li[:len(l)//2])/len(li[:len(l)//2])
ll2 = sum(li[(len(li)//2)+1:])/len(li[(len(li)//2)+1:])
if ll1 == ll2:
    print("yes")
else:
    print("no")
