# x=str(input("Enter the Name: "))
# y=int(input("Enter his\her age: "))
# if(y>=18):
#     print(x,"is eligible for voting")
# else:
#     print(x,"is not eligible for voting")



def Func(S):
  W = S.split(" ")
  for i in range(len(W)):
     
      
      W[i]=W[i].lower()  
  S = sorted(W)
  print(' '.join(S))
 

S = "python is interpreted"
 

Func(S)




text="python is interpreted"
for i in text.split():
    
    print(i)
  












