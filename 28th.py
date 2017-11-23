alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#mystr = input('enter your string here: ')
mystr = 'If You Use Weather Forecasts For Anything, You Need To Know About The JPSS Satellite'
print('\n'+'-'*10+'Problem 1'+'-'*10)
for temp in alph:
	cnt = mystr.count(temp)
	if(cnt != 0):
		print('%s count = %d'%(temp, cnt))


print('\n'+'-'*10+'Problem 2'+'-'*10)
