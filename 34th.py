def t1():	
	print('-'*10+'t1 start'+'-'*10)
	print('This is the code of function t1()')
	print('-'*10+'t1 end'+'-'*10)

def t2():
	print('-'*10+'t2 start now'+'-'*10)
	t1()
	print('-'*10+'t2 ends now'+'-'*10)

t2()

print('\n' + '-'*10 + 'Calling function' + '-'*10 + '\n')

def pl():
	print('-'*30)
	
def pml(num):
	i = 0
	while(i < num):
		pl()
		i+=1

pml(4)
