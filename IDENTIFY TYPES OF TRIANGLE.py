#IDENTIFY TYPES OF TRIANGLES
def triangles():
        print("Input lengths of the triangle sides: ")
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))

        if a == b == c:
                print("Equilateral triangle")
        if a==b or b==c or c==a:
                print("isosceles triangle")
        else:
                print("Scalene triangle")

        if a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
           print('this is a right triangle')
triangles()           
