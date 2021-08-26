#reversing digits
def rd():
  n=int(input('enter a number  '))
  while(n>0):
    rdn=0
    ud=n%10#FOR GETTING THE LAST DIGIT
    n=n//10
    rdn=rdn*10+ud#TO GET THE PREVIOUS NUMBER TO NEXT PLACE
    print(rdn)
rd()
