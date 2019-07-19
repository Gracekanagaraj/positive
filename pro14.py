nn11,nn21=list(map(int,input().split()))
lit1=list(map(int,input().split()))
lit2=[]
while(nn21):
	k = list(map(int,input().split()))
	lit2.append(k)
	nn21-=1
for i in lit2:
	val=0
	for j in range(i[0]-1,i[1]):
		val=val^lit1[j]
	print(val)
