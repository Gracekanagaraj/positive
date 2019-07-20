Num=int(input())
LIS1=list(map(int,input().split()))
for i in LIS1:
	if LIS1.count(i)==1:
		print(i)
		break
