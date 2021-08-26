def sod():
    #SUM OF DIGITS
    n=int(input("Enter a number:"))
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig#GETTING THE LAST DIGIT
        n=n//10
    print("The total sum of digits is:",tot)
sod()
