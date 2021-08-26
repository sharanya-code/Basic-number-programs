#RANDOM NUMBER GUESSING GAME 
import random#GETTING RANDOM IMPORT
n = random.randint(1, 99)
g = int(input("ENTER A NUMBER FROM 1-99: "))#INPUT A NUMBER
while n != g:
    print
    if g < n:#GUESS APPROXIMATION
        print ("guess is low")
        g = int(input("ENTER A NUMBER FROM 1-99: "))
    elif g > n:
        print ("guess is high")
        g = int(input("ENTER A NUMBER FROM 1-99: "))
    else:
        print ("YOU GUESSED IT! YAY!")
        break

print("THANKS FOR PLAYING THE GAME")
