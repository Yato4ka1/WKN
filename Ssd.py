import sys
x=int(sys.argv[1])
num1 = x // 100
num2 = x // 10 % 10
num3 = x % 10
print((num1 + num2 + num3) / 3)