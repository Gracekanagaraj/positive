Dki=input()
Qti=[]
for X in Dki:
  if X not in Qti:
    Qti.append(X)
  else:
    break  
print(len(Qti))
