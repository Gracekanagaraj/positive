kt=input()
l=[0]
if "ab" not in kt:
	print("0")
else:
	for i in range(len(kt)):
		c=1
		for j in range(i,len(kt)-1):
			if kt[j]=="a" and kt[j+1]=="b":
				c=c+1
			elif kt[j]=="b" and kt[j+1]=="a":
				c=c+1
			else:
				l.append(c)
				c=1
				break
		if kt[i]=="a":
			l.append(c)
		else:
			l.append(c-1)
	print(max(l))
