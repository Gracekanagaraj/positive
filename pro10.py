a12=int(input())
b12=list(map(int,input().split()))
c1=0
for m in range(0,a12):
	for p in range(0,m):
		if b12[p]<b12[m]:
			c1=c1+b12[p]
print(c1)
