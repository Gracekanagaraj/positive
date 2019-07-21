import sys,string
num = int(input())
Lt = [ int(x) for x in input().split()]
s2 = 0
for i in range(0,num) :
    s2 = s2 + Lt[i]

for j in range(num-2,-1,-1) :
    for i in range(0,num-j) :
        li, ri = i,j+i
        sum1 = sum(Lt[li:ri+1])
        if sum1 > s2 :
            s2 = sum1
print(s2)
