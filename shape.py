class shape():
    def __init__(self,n):
        self.n=n
    def triangle(self):
        self=3
        print("This is Triangle")
        while True:
            a=int(input("Enter the First side: "))
            b=int(input("Enter the second side: "))
            c=int(input("Enter the third side: "))
            if a==b!=c or a!=b==c or a==c!=b:
                print("It is a isosceles triangle")
                break
            elif a==b==c:
                print("It is a equilateral triangle")
                break
            else:
                print("It is a scalene triangle")
                break
    def rectangle(self):
        self=4
        print("This is Rectangle")
        while True:
            a=int(input("Enter the First side: "))
            b=int(input("Enter the second side: "))
            c=int(input("Enter the third side: "))
            d=int(input("Enter the fourth side: "))
            if a==b==c==d:
                print("It is a square")
                break
            else:
                print("It is a Rectangle")
                break
    def pentagon(self):
        self=5
        print("This is Pentagon")
        while True:
            a=int(input("Enter the First side: "))
            b=int(input("Enter the second side: "))
            c=int(input("Enter the third side: "))
            d=int(input("Enter the fourth side: "))
            e=int(input("Enter the Fifth side: "))
            if a==b==c==d==e:
                print("It is a Regular Pentagon")
                break
            else:
                print("It is a ractangle Pentagon")
                break
    def hexagon(self):
        self=6
        print("This is Hexagon")
        while True:
            a=int(input("Enter the First side: "))
            b=int(input("Enter the second side: "))
            c=int(input("Enter the third side: "))
            d=int(input("Enter the fourth side: "))
            e=int(input("Enter the Fifth side: "))
            f=int(input("Enter the sixth side: "))
            if a==b==c==d==e==f:
                print("It is a Regular Hexagon")
                break
            else:
                print("It is a Hexagon")
                break
    def heptagon(self):
        self=7
        print("This is Heptagon")
        while True:
            a=int(input("Enter the First side: "))
            b=int(input("Enter the second side: "))
            c=int(input("Enter the third side: "))
            d=int(input("Enter the fourth side: "))
            e=int(input("Enter the fifth side: "))
            f=int(input("Enter the sixth side: "))
            g=int(input("Enter the seventh side: "))
            if a==b==c==d==e==f==g:
                print("It is a Regular Heptagon")
                break
            else:
                print("It is a Heptagon")
                break
    def octagon(self):
        self=8
        print("This is Octagon")
        while True:
            a=int(input("Enter the First side: "))
            b=int(input("Enter the second side: "))
            c=int(input("Enter the third side: "))
            d=int(input("Enter the fourth side: "))
            e=int(input("Enter the Fifth side: "))
            f=int(input("Enter the sixth side: "))
            g=int(input("Enter the seventh side: "))
            h=int(input("Enter the eighth side: "))
            if a==b==c==d==e==f==g==h:
                print("It is a Regular Octagon")
                break
            else:
                print("It is a Octagon")
                break
    
m=print("Find the figure")
obj1=shape(m)
while True:
    n=int(input("Number of sides:"))
    if n==3:
        obj1.triangle()
    elif n==4:
        obj1.rectangle()
    elif n==5:
        obj1.pentagon()
    elif n==6:
        obj1.hexagon()
    elif n==7:
        obj1.heptagon()
    elif n==8:
        obj1.octagon()
    else:
        print("Figure not found")
    break