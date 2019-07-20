ni, mi = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
flag = 1
for i in range(0, len(l2)):
    if li2[i] not in li1:
        flag = 0
        break
if flag:
    print('YES')
else:
    print('NO')
