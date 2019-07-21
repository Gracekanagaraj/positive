import sys
def palindrome(dki):
    if len(dki) == 1:
        return False
    if dki == dki[::-1]:
        return True
    return False
dki = input()
n1 = len(dki)
for i in range(n1-1, 0, -1):
    for j in range(0, n1-i):
        i1 = j
        i2 = j+i+1
        d2 = dki[i1:i2]
        if palindrome(d2):
            print(n1-len(d2))
            sys.exit()
