number1=int(input())
aag=list(map(int,input().split()))
p1=[]
q1=[]
for i in range(len(aag)):
	if i%2==0:
		p1.append(aag[i])
	else:
		q1.append(aag[i])
s1=sum(p1)
r1=sum(q1)
if(s1>r1):
	print(s1)
else:
	print(r1)
