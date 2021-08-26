#Fibonacci series
def fibo(n):
    i = 0
    a = 0
    b = 1
               
    while(i < n):#INFINITE LOOP
        if(i <= 1):#FOR FIRST NUMBER
            c = i
        else:
            c=a+b#FOR NEXT TERMS IN SERIES
            a = b
            b=c
        return(c)
        i = i + 1

k=int(input('enter the number of terms'))
print(fibo(k))
        
