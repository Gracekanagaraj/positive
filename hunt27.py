kb=input()
n=len(kb)
def check_palindrome(kb,n):
    if kb==kb[-1:-n-1:-1]:
        n-=1
        kb=kb[0:n]
        check_palindrome(kb,n)
    else:
        print(kb)
check_palindrome(kb,n)   
