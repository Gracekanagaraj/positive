ppi, Qpi, Fpi, Kdi = map(int, input().split())
cnt = 0
Dv = Qpi-Fpi
if (Dv >= 0):
    S1 = (ppi-Fpi)*2
    for X in range (Kdi):
        if (X == Kdi-1):
             S1 =S1/ 2
        if (Dv < S1):
            Dv= Qpi
            cnt += 1
        Dv = Dv - S1
        if (Dv < 0):
            cnt = -1
            break
        S1 = 2*ppi - S1
    print (cnt)
else:
    print (-1)
