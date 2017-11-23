info = {'name':'Monica', 'id':100, 'gender':'f', 'address':'Beijing, China', 'age':25}

print('-'*10 + 'Traverse the key' + '-'*10)
for key in info.keys():
	print('key =', key)


print('-'*10 + 'Traverse the value' + '-'*10)
for value in info.values():
	print('value =', value)


print('-'*10 + 'Traverse the items' + '-'*10)
for item in info.items():
	print('item =', item)


print('-'*10 + 'Traverse the key-value' + '-'*10)
for key, value in info.items():
	print('key = %s, value = %s'%(key, value))
