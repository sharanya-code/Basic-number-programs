#perfect number
def pn():
  n=int(input('enetr a number  '))
  s=0
  for i in range(1,n,1):
    if n%i==0:
      s=s+i#FOR SUM OF FACTORS
  if n==s:
      print('its a perfect number')

  else:
      print('its not a perfect number')
pn()
