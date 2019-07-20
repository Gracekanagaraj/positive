brry=input()
for i in range(1,len(brry)):
    if ord(brry[i])>ord(brry[0]):
        answer=brry[i:]
        break
print(answer)
