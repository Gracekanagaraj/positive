s1,t1 = map(int,input().split())
l11 = []
l21 = []
l11 = input().split()
for i in range(len(l11)):
    l11[i] = int(l11[i])
for i in range(t1):
    a,b = map(int,input().split())
    res = 0
    for i in range(a-1,b):
        res += l11[i]
    print(res)
