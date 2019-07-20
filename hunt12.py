try:
    st,pq=map(int,input().split())
    arsy=list(map(int,input().split()))
    ars1=sorted(arsy)
    print(ars1[st-pq])
except ValueError:
    print("invalid")
