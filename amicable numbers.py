def amicable():
  #amicable numbers
  n=int(input('enter a number  '))
  z=int(input('enter a  number  '))
  sof1=0
  sof2=0
  for i in range(1,n,1):#CHECKING THE SUM OF FACTORS
    if n%i==0:
      sof1+=i
  for j in range(1,z,1):
    if z%j==0:
      sof2+=j
  if sof1==z and sof2==n:
      print('they are amicable')
  else:  
      print('they are not amicable')
amicable()
