pi3=int(input())
while pi3%10==0:
  pi3=pi3//10
pi3=str(pi3)
re=pi3[::-1]
if pi3==re:
  print("yes")
else:
    print("no")
