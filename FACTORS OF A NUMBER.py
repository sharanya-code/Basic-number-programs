#FACTORS OF A NUMBER
def factor():
   x=int(input('enter a number '))
   for i in range (2,x+1,1):
      if x%i==0:
         print(i)
factor()
