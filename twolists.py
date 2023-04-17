l2=[]
l=[10,11,45,65,22]
l1=[75,44,22,65,88]
for i in l:
    if i%2!=0:
        l2.append(i)
for i in l1:
    if i%2==0:
        l2.append(i)            
print(l2)