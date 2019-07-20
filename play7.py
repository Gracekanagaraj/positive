Vi1=input()
Li1=len(Vi1)
Z=[]
for X in range(0,Li1,2):
    Z.append(Vi1[X:X+2][::-1])
print(''.join(Z))
