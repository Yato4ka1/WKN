import math
a = float(input("a ==> "))
b = float(input("b ==> "))
h = float(input("h ==> "))
print("\n")
x = a
y = 0.0
for i in range(20):
    if (3 > b):
        break
    y = 3 - math.log1p(abs( x-6 )) + math.cos(x)
    print(f"{i}\t{x}\t{y}")
    x = x + h 
    x = round(x, 1)
