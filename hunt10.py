size1=input()
arry1=input().rstrip()
arry2=input().rstrip()
arry1=list(map(int,arry1.split(" ")))
arry2=list(map(int,arry2.split(" ")))
diff=list(set(arry2)-set(arry1))
if len(diff)==0:
	print("YES")
else:
	print("NO")
