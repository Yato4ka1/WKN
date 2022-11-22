data = dict()

key1 = input ('Назва першої компанії:  ')
key2 = input ('Назва другої компанії:  ')
key3 = input ('Назва третьої компанії: ')
key4 = input ('Назва четвертої компанії:  ')

data[key1] = int (input ('Введіть активи компанії '+key1+': '))
data[key2] = int (input ('Введіть активи компанії '+key2+': '))
data[key3] = int (input ('Введіть активи компанії '+key3+': '))
data[key4] = int (input ('Введіть активи компанії '+key4+': '))

tup = ()

def get_key(data,value):
    for k,v in data.items():
        if v == value:
            return k

tup = (data[key1],data[key2],data[key3],data[key4])

sum1 = sum (tup)
print ('\n')
print ('Сумарні активи компаній:  '+str(sum1))
print ('Компанія з найбільшими активами:  '+get_key(data, max(tup)))
print ('Компанія з найменшими активами:  '+get_key(data, min(tup)))
print (data)