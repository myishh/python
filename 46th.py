def print_line(char, cnt, num):
	i = 0
	while i < cnt:
		print(char * num)
		i += 1
	

print_line('$', 5, 30)

print('-'*20 + 'input para' + '-'*20)

char = input('enter a char')
cnt = int(input('enter cnt'))
num = int(input('enter num'))

print_line(char, cnt, num)
