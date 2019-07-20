kt,s = map(int,input().split())
v1 = list(map(int,input().split()))
b,n = 0,[]
for i in range(0,len(v1)):
  kt = i
  for p in range(0,len(v1)):
    for l in range(0,s):
      if l == s-1:
        try:
          b += v1[p+i]
        except IndexError:
            kt = kt-1
            b +=v1[kt]
      else:
        b += v1[i]
    n.append(b)
    b = 0
for i in range(0,len(v1),s):
  b = sum(v1[i:i+s])
  n.append(b)
print(*sorted(set(n)))
