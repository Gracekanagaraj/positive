ci=int(input())
di=list(map(int,input().split()))
a1=0
vi=[]
for i in range(0,ci):
	if(di[i]==i):
		temp=di[i]
		a1=1
		vi.append(temp)
		vi=sorted(vi)
print(*vi)
if(a1==0):
	print(-1)
