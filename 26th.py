usrname = 'myishh'
password = '998998'

un = input('plz enter user name:')
pwd = input('plz enter your password:')

if (un == usrname and pwd == password):
	print('good')

print('*'*30 + '\n')
level = 5
cnt = 0
while cnt < 5:
	cnt = cnt + 1
	print('*' * cnt)
while cnt > 0:
	cnt = cnt - 1
	print('*' * cnt)
