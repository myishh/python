info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

print(info['name'])
print(info['address'])

newid = 1024 #int(input('plz enter new stuID: '))
info['id'] = newid
print('new StuID = %d'%info['id'])

info['age'] = 28
print('info[\'age\'] =', info['age'])
print('info =', info)

del info['sex']
print('info =', info)

print('len of info = %d'%len(info))
print('keys of info =', info.keys())
print('values of info =', info.values())
print('items of info =', info.items())
print('info has key \'name\'', info.has_key('name'))
