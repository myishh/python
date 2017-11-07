import os
files = [d for d in os.listdir('.')]
print('=====List all files and dirs of a directory=====')
print(files)

print('-----double loop-----')
strings = [m + n for m in 'ABC' for n in 'XYZ']
print(strings)

print([x*x for x in range(1,11) if x % 2 == 0])
print([x*x for x in range(1,11)])
