import sys,string, math, itertools
num,k = input().split()
num,k = int(num),int(k)
L = [ int(x) for x in input().split()]
for i in range(0,num) :
    if (86400-L[i]) >= k :
        print(i+1)
        sys.exit()
    k -= (86400-L[i])
