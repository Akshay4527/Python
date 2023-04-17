# n=int(input("Enter the First Number: "))
# if n == 1:
#     print(n, "is not a prime number")
# elif (n % 2) == 0:
#     print(n, "is not a prime number")
# elif (n % 3) == 0:
#     print(n, "is not a prime number")
# elif (n % 5) == 0:
#     print(n, "is not a prime number")
# elif (n % 7) == 0:
#     print(n, "is not a prime number")
# else:
#     print(n, "is a prime number")







n=int(input("Enter a number: "))
f=False
if n==1:
    print(n, "is not a prime number")
elif n==0:
    print(n, "is not a prime number")
elif n > 1:
    for i in range(2, n):
        if n%i==0:
            f=True
            break
    if f:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")









n = int(input("Enter a number: "))
if n == 1:
    print(n, "is not a prime number")
elif n == 0:
    print(n, "is not a prime number")
count=0
while 1 < n:
    for i in n:
        if n % i == 0:
            count=count+1
        i=i+1
    break
if count == 0:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
