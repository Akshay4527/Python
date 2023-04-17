l=[10,20,30,100,150]
l[0]=150
l[4]=10
print(l)



a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=int(input("Enter d: "))
e=int(input("Enter e: "))
l=[a,b,c,d,e]
l[0]=e
l[4]=a
print(l)





l=["Happy","Sad","Angry"]
print(l)
a=(input("Select an Emotion: "))
if(a=="Happy"):
    print("😁")
elif(a=="Sad"):
    print("😓")
elif(a=="Angry"):
    print("😤")
else:
    print("Emotion not found")
