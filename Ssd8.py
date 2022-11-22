from array import *
from numpy import *
from random import *

N = int (input ('Розмір матриці:  '))
matrix1 = eye(N, dtype=int)

for i in range(N):
    for j in range(N): 
        matrix1[i][j] = randint(0,13)

spisok = []
for i in range(N):
    for j in range(N): 
        if i == j:
           m = matrix1[i][j]*matrix1[i][j]
           spisok.append (m)

print (matrix1)
print ('Добуток елементів:  '+str(spisok))

tmp = []

for i in range(N):
    for j in range (N):
        if matrix1[i][j] in tmp:
            matrix1[i][j] = 0
        tmp.append(matrix1[i][j])
print (matrix1)

