import re
s= 'sat mat cat rat pat'
x= re.findall('[spr]at',s)
y=re.findall('[smcrp]at',s)
print(x)
print(y)