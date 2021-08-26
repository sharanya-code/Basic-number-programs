from math import factorial
"""
1
11
121
1331
"""
num = int(input("Enter the number"))
        
for i in range (0,num):
    print('\n')
    for j in range(0,i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end = " ")
