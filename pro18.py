n1,m1=map(int,input().split())
l1=[]
for _ in range(n1):
	l1.append(input())
for i in range(len(l1)):
	if('0' in l1[i]):
		l1[i]=l1[i].replace('0','')
	l1[i]=l1[i].replace(' ','')
lengths=[]
for i in l1:
	if(len(i)>0):
		lengths.append(len(i))
m1=min(lengths)
final_ans='11 '*m1
final_ans=final_ans.strip()
for i in range(m1):
	print(final_ans)
