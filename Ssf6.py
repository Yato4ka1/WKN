import math 
a = float(input("a ==> ")) 
b = float(input("b ==> ")) 
h = float(input("h ==> ")) 
x = a 
y = 0.0 
lst = [] 
for i in range(20): 
    if 3 > b: 
        break 
    y = 3 - math.log1p(abs( x-6 )) + math.cos(x)
    y= round(y,2) 
    lst.append(y) 
    print(i, ") ", lst[i]) 
    x = x + h 
    x = round(x, 1)
print(lst)