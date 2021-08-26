#PRIME NUMBERS
def pn():
    b=int(input("enter a number:  "))
    for i in range (2,b//2+1,1):#CHECKING FOR FACTORS
        if b%i==0:
            print('not prime') 
    else:
        print('prime')
pn()
