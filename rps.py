import random
l=["Rock","Paper","Scissors"]
print(l)
com=(random.choice(l))
user=input("Enter a Choice: ")

print(com)
if user==com:
    print("The Game is a Tie")
elif user=="Rock" and com=="Scissors":
    print("You Won!!!")
elif user=="Scissors" and com=="Paper":
    print("You Won!!!")
elif user=="Paper" and com=="Rock":
    print("You Won!!!")
elif com=="Rock" and user=="Scissors":
    print("You Lose!!!")
elif com=="Scissors" and user=="Paper":
    print("You Lose!!!")
elif com=="Paper" and user=="Rock":
    print("You Lose!!!")
else:
    print("Enter a valid option")
