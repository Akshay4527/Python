class circle:
    def __init__(self):
        self.radius=0
    def area(self):
        print("Area:",3.14*self.radius**2)
    def circumference(self):
        print("Circumference:",2*3.14*self.radius)
c=circle()
c.radius=int(input("Enter the Radius: "))
c.area()
c.circumference()








class circle:
    def __init__(self,radius):
        self.radius=radius
radius=int(input("Enter the Radius: "))
c=circle(radius)
print("Circumference:",2*3.14*c.radius)
print("Area:",3.14*c.radius**2)