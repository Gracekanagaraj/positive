a1=input()
b1=input()
b1=b1.split()
b1.sort(reverse = True)
d=""
for i in b1:
	d+=i
print(int(d))
