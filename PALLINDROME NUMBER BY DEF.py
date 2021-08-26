def rev(n):
    rdn=0
    n1=n
    while(n1>0):
        ud=n1%10
        rdn=rdn*10+ud
        n1=n1//10
    return rdn

N=int(input('ENTER A NUMBER: '))

if N == rev(N):
    print('these numbers are a pallindrome')

else:
    print('they are not a pallindrome')
            
