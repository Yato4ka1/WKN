A = set()
for i in range (1,26):
    A.add (i)


B = set ()
for elem in list(A):
    if elem%3:
       B.add (elem)
B = A - B
C = A - B
print ('Множина натуральних чисел від 1 до 25:  '+str(A))
print ('Множина всіх чисел с А, що діляться на 3:  '+str(B))
print ('Множина всіх чисел з А, що не діляться на 3:  '+str(C))