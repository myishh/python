f = open('35th.py', 'r')
#f.write('print(\'This is a good Day!!\')')
content = f.readlines()
i = 0
for tem in content:
	print('%d:%s'%(i, tem), end='')
	i += 1

f.close()
