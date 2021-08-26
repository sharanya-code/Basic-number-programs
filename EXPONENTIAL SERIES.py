def exp():
   #SUM OF EXPONENTIAL SERIES
   x=float(input('enter a number '))
   n=int(input('enter a number '))
   sum1=1
   for i in range(2,n+1,1):
      sum1=sum1+((x**i)/i)#RESPONISIBLE FOR EXPONENTIAL AND DENOMENATOR INCREMENT
   print(sum1)
exp()
