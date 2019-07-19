li = []
a,b1 = input().split()
b1 = int(b1)
li1 = list(map(int,input().split()))

for i in range (0,len(li1)-1):
	for j in range (i+1i,len(li1)):
		sum1 = li1[i]+li1[j]
		li.append(sum1)
if b1 in li:
	print ('yes')
else:
