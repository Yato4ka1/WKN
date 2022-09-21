import math
x = float(input())
a = 3 * math.tan(x)
b = math.log(math.cos(x)) + 4
c = abs(x - x ** 2)
print(a / b + c)