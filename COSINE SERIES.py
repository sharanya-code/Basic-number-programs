def cosine_series():
    #cosine series summation
    x=float(input('enter a number '))
    n=int(input('enter a number '))
    s=1
    t=1
    for i in range(1,n+1,1):
        t=t*-1*x*x/(2*i)*(2*i-1)#DENOMENATOR AND FACTORAL INCREMENT
        s=s+t
    print(s)
cosine_series()
