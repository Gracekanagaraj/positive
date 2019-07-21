num=[int(s) for s in input().split()]
mi=[int(s) for s in input().split()]
f=1
for i in range(num[0]):
    for j in range(num[0]):
        if i!=j:
            if num[1]==mi[i]+mi[j]:
                f=0
                break
if f==0:
    print('YES')
else:
    print('NO')
