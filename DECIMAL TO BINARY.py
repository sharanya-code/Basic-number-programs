#DECIMAL TO BINARY
n=int(input('enter a number '))
e=1
bn=0
while(n>0):#loop for binary to decimal
   d=n%2
   e=e*10
   bn=e*d+bn
   n=n//2
   
print(bn)
