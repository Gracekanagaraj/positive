gj,st=map(int,input().split())
cs1=list(map(int,input().split()))
ds=[[abs(i-st),i] for i in cs1]
ds.sort()
ds=ds[1:]
e=[i[1] for i in ds[:3]]
print(*e)
