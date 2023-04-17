# def detail(i):
#     x = [20,21,22,23]
#     if i in x:
#         print("Roll number",i, "is present")
#     else:
#         print("Roll number",i, "is absent")
# i=int(input("Enter a Roll number: "))
# detail(i)



# def detail():
#     count=0
# text=input("Enter a word: ")
# r=['a','e','i','o','u']
# if r in text:
#     count+=1

s=''
count=0
text=input("Enter a word: ")
for i in text:
        s+=i
        count+=1