bbi,s=map(str,input().split("|"))
c=input()
if  len(bbi)>len(s):
    if len(bbi)==len(s)+len(c):
        print(bbi+"|"+s+c)
elif len(bbi)<len(s):
     if len(s)==len(bbi)+len(c):
        print(bbi+c+"|"+s)
elif len(bbi)==len(s) and len(c)>1 or (len(s) or len(bbi)):
    print("impossible")
