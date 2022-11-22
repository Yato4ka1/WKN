from array import *

N = int (input ('Number:  '))

masiv1 = array ('i', [])

for i in range (1,N+1):
    masiv1.append (i)
masiv1 = array ('i', masiv1)

spisok = []
for elem in masiv1:
    if N%elem==0:
        spisok.append(elem)

masiv1 = array('i', spisok)

max_masiv1 = max (masiv1)
min_masiv1 = min (masiv1)
print (masiv1)

masiv1.remove (max_masiv1)
masiv1.remove (min_masiv1)

print (masiv1)
