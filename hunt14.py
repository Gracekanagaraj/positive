from itertools import permutations
si=input()
di=permutations(si)
for i in list(di):
  print("".join(i))
