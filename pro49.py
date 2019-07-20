si=input()
ti=input()
c=1
n=len(si)
for i in range(0,len(ti)-n,n):
	if ti[i:i+n]==si:
		c=c+1
print(c)
