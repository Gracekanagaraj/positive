kt=int(input())
s=[int(i) for i in input().split()]
a=[]
for i in range(0,kt):
    c=1
    for j in range(i,kt):
        c=c*s[j]
    a.append(c)
for i in range(0,kt):
    c=1
    for j in range(i+1):
        c=c*s[j]
    a.append(c)
print(max(a))
