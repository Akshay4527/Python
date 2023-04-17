# class temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
# celsius=int(input("Enter the celsius: "))
# c=temperature(celsius)
# print("Fahrenheit:",c.celsius*1.8+32)




######### mistake ########
# class temperature:
#     def __init__(self,celsius,fahrenheit):
#         self.celsius=celsius
#         self.fahrenheit=fahrenheit
# celsius=int(input("Enter the celsius: "))
# c=temperature(celsius)
# print("Fahrenheit:",c.celsius*1.8+32)
# fahrenheit=int(input("Enter the fahrenheit: "))
# c=temperature(fahrenheit)
# print("Celsius:",(c.fahrenheit-32)*1.8)





class temperature:
    def __init__(self,n):
        self.n=n
    def Fahrenheit(self):
        print("Celsius:",(self.n-32)*5/9)
    def Celsius(self):
        print("Fahrenheit:",self.n*(9/5)+32)
n=int(input("Enter the temperature in Celsius: "))
c=temperature(n)
c.Fahrenheit()
n=int(input("Enter the temperature in fahrenheit: "))
c=temperature(n)
c.Celsius()