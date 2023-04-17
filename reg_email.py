import re
x=input("Enter your E-Mail: ")
y = re.search("[a-z]+[_&]*[0-9]*@[a-z]{0,5}.[a-z]{2,3}", x)
if y:
    print("Login Sucessfulley")
else:
    print("Email must contain [a-z][_&][0-9]@gmail.com")