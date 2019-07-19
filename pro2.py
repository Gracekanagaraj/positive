from itertools import combinations
Si,u=map(int,input().split())
li=len(str(Si))
lst=list(combinations(str(Si),li-u))
lst=sorted(lst)
print(*lst[0],sep='')
