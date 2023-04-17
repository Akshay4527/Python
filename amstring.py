s=input("Enter a number: ")
n=len(s)
x=0
for i in s:
    x+=int(i)**n
S=int(s)
if S==x:
        print(s, "is a amstring number")
else:
        print(s, "is not a amstring number")
 