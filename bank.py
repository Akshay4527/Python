class bank:
    def __init__(self,n):
        self.n=n
    def account1(self):
        self.n=457
        self.t=500
        print("\tName: Jobin""\n","\tAccont Number:32290010003457""\n""\tIFSC Code: IOB3229007")
        print("1.Deposite","2.Withdraw","3.Balance","4.Exit")
        while True:
            user=int(input("Select any option: "))
            if user==1:
                self.d=int(input("Enter the amount to be deposited: "))
                self.t=self.t+self.d
                print("Amount Deposited:",self.d,"\t New Balance:",self.t)
            elif user==2:
                self.w=int(input("Enter the amount to be withdrawed: "))
                if self.t<self.w:
                    print("Insufficient Balance")
                else:
                    self.t=self.t-self.w
                    print("Amount Withdrawed:",self.w,"\t New Balance:",self.t)
            elif user==3:
                print("Balance:",self.t,"rs")
            elif user==4:
                break

    def account2(self):
        self.n=458
        self.t=800
        print("\tName: Aswin""\n","\tAccont Number:32290010003458""\n""\tIFSC Code: IOB3229007")
        print("1.Deposite","2.Withdraw","3.Balance","4.Exit")
        while True:
            user=int(input("Select any option: "))
            if user==1:
                self.d=int(input("Enter the amount to be deposited: "))
                self.t=self.t+self.d
                print("Amount Deposited:",self.d,"\t New Balance:",self.t)
            elif user==2:
                self.w=int(input("Enter the amount to be withdrawed: "))
                if self.t<self.w:
                    print("Insufficient Balance")
                else:
                    self.t=self.t-self.w
                    print("Amount Withdrawed:",self.w,"\t New Balance:",self.t)
            elif user==3:
                print("Balance:",self.t,"rs")
            elif user==4:
                break

    def account3(self):
        self.n=456
        self.t=1000
        print("\tName: Suhail""\n","\tAccont Number:32290010003456""\n""\tIFSC Code: IOB3229007")
        print("1.Deposite","2.Withdraw","3.Balance","4.Exit")
        while True:
            user=int(input("Select any option: "))
            if user==1:
                self.d=int(input("Enter the amount to be deposited: "))
                self.t=self.t+self.d
                print("Amount Deposited:",self.d,"\t New Balance:",self.t)
            elif user==2:
                self.w=int(input("Enter the amount to be withdrawed: "))
                if self.t<self.w:
                    print("Insufficient Balance")
                else:
                    self.t=self.t-self.w
                    print("Amount Withdrawed:",self.w,"\t New Balance:",self.t)
            elif user==3:
                print("Balance:",self.t,"rs")
            elif user==4:
                break

    def account4(self):
        self.n=459
        self.t=1200
        print("\tName: Adersh""\n","\tAccont Number:32290010003459""\n""\tIFSC Code: IOB3229007")
        print("1.Deposite","2.Withdraw","3.Balance","4.Exit")
        while True:
            user=int(input("Select any option: "))
            if user==1:
                self.d=int(input("Enter the amount to be deposited: "))
                self.t=self.t+self.d
                print("Amount Deposited:",self.d,"\t New Balance:",self.t)
            elif user==2:
                self.w=int(input("Enter the amount to be withdrawed: "))
                if self.t<self.w:
                    print("Insufficient Balance")
                else:
                    self.t=self.t-self.w
                    print("Amount Withdrawed:",self.w,"\t New Balance:",self.t)
            elif user==3:
                print("Balance:",self.t,"rs")
            elif user==4:
                break

m=print("Hello")
obj1=bank(m)
while True:
    n=int(input("Enter your Account Number:"))
    if n==457:
        obj1.account1()
    elif n==458:
        obj1.account2()
    elif n==456:
        obj1.account3()
    elif n==459:
        obj1.account4()
    else:
        print("Invalid Account")
        break
