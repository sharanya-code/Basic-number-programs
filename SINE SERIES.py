#sine series summation
print('sum ',s)
x=float(input('enter a number '))
n=int(input('enter a number '))
s=x
t=1
for i in range(1,n+1,1):
  t=t*-1*x*x/(2*i)*(2*i-1)#RESPONSIBLE FOR FACORIAL AND DENOMENATOR INCREMENT
  s=s+t
  print('sum ',s)
