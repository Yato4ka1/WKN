import math
x=float(input(""))
def f1(x1):
    rez=math.sin(x)
    return(rez)
def f2(x2):
    rez=math.cos(x)
    return(rez)
def f3(x3):   
    rez=math.tan(x)
    return(rez)
y=0.0
if x >= 3: 
    y=f1(x)
elif 0 <= x < 3:
    y=f2(x)
elif x < 0:
    y=f3(x)
print(y)