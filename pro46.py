pi3=int(input())
qi3=list(map(int,input().split()))
a3=0
b3=0
qi3.sort(reverse=True)
for i in qi3:
  qi3=a3+i
  if b3>qi3:
    a3=qi3
  else:
    a3=b3
    b3=qi3
print(a3,b3)
