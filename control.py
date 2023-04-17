# for i in range(0,6):
#     if i==3:
#         break
#     print(i)



# text="Hello"
# for i in text:
#     if i=="e":
#         break
#     print(i)





s=''
count=0
text="3hello45python456"
for i in text:
    if i.isdigit():
        s+=i
        count+=1

        if count==3:
            break
print(s)
