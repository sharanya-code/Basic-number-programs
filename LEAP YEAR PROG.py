#LEAP YEAR
def leap():
   a=int(input('enter a number'))
   if a%4==0 and a%400==0:#TO CHECK FOR LEAP YEAR
      print('leap year')

   else:
      print('not leap year')
leap()
