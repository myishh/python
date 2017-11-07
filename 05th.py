#coding=utf-8

print(True and True)
print(True and False)
print(False and False)
print(5 > 4)
print(3 > 6)

a = 123
print(a)
a = False
print(a)
a = 'MotherFucker'
print(a)

a = 'Global Risk'
b = a
print('id of a = %d'%id(a))
print('id of b = %d'%id(b))
a = 'Commando'
print('id of a = %d'%id(a))
print('id of b = %d'%id(b))
