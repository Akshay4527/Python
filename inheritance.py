## Single inheritance

# class person:
#     def __init__(self):
#         self.name="Alex"
#         self.age="21"
#         print("Student Details")
# class student(person):
#     def __init__(self):
#         super().__init__()
#         print(self.name,self.age)
#         print("S6 Computer Science")
# stud=student()


## Multiple Inheritance

class Cat:
    def puzz(self):
        print("It is a Cat")
        print("You can call him:",n)

class Dog:
    def Dogs(self):
        print("It is a Dog")
        print("You can call him:",m)

class Pet(Cat,Dog):
    def __init__(self):
        super().puzz()
        super().Dogs()
        print("These all are under Pet category")
n=input("Give a Name for the cat: ")
m=input("Give a Name for the dog: ")
p=Pet()