number = int(input())
mylist1 = list(map(int,input().split()))
for i in range(number):
    for j in range(number):
        for k in range(number):
            if(mylist1[i]+mylist1[j]==mylist1[k]) and i<j<k:
                print('{} {} {}'.format(mylist1[i],mylist1[j],mylist1[k]))
