gp = int(input())
ai = list(map(int,input().split()))
ss,l3 = 0,[]
b3 = [x for x in range(1,gp+1)]
for i in ai:
  if i in b3:
    b3.remove(i)
kh = 0
for i in range(0,gp-1):
  p = ai[i]
  for j in range(i+1,gp):
    if p == ai[j]:
      if p < b3[kh]:
        ai[j] = b3[kh]
        ss += 1
      else:
        ai[i] = b3[kh]
        ss += 1
      kh += 1
print(ss)
print(*ai)
