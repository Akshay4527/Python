l=[]
sum=0
i=0
while 1<10:
    dict={"Shirt":700,"T-shirt":400,"Jeans":1000,"Watch":1300}
    print("1. Shirt")
    print("2. T-shirt")
    print("3. Jeans")
    print("4. Watch")
    print("5. Exit")
    choice=int(input("Enter your choice(1-5):"))
    if choice==1:
        sum+=dict["Shirt"]
        l.append("Shirt")
        print(sum)
        i += 1
    elif choice==2:
        sum+=dict["T-shirt"]
        l.append("T-shirt")
        print(sum)
        i += 1
    elif choice==3:
        sum+=dict["Jeans"]
        l.append("Jeans")
        print(sum)
        i += 1
    elif choice==4:
        sum+=dict["Watch"]
        l.append("Watch")
        print(sum)
        i += 1
    elif choice==5:
        print("On Your Cart ",l)
        print("Total Amount",sum)
        break
    else:
        print("Wrong Choice")