Pji,Qji=map(int,input().split())
Li=list(map(int,input().split()))[:Pji]
rd=int(input())
S=(sum(Li)-Li[Qji])//2
if (S==rd):
    print("Bon Appetit")
else:
    print(abs(S-rd))
