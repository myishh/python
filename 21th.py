print('我们已经知道，可以直接作用于for循环的数据类型有以下几种: ')
print('一类是集合数据类型，如list、tuple、dict、set、str等;')
print('一类是generator，包括生成器和带yield的generator function;')
print('这些可以直接作用于for循环的对象统称为可迭代对象：Iterable;')
print('*****使用isinstance()判断一个对象是否是Iterable对象*****')
from collections import Iterable
result = isinstance([], Iterable)
print('isinstance([], Iterable) = ', result)
print('isinstance({}, Iterable) = ', isinstance({}, Iterable))
print('isinstance(\'abc\', Iterable) = ', isinstance('abc', Iterable))
print('isinstance((x for x in range(10)), Iterable) = ', isinstance((x for x in range(10)), Iterable))
print('isinstance(100, Iterable) = ', isinstance(100, Iterable))

print('******** done ********\n')
