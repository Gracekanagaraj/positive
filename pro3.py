st1,st2=input().split()
cost_diff=abs(len(st1)-len(st2))
for i in range(len(st1)):
    if len(st2)==1 and st2[i] in st1:
        break
    if st1[i] != st2[i]:
        cost_diff+=1 
print(cost_diff)
