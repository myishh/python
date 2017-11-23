class f1:
	pass

class s1(f1):
	
	def show(self):
		print('s1.show' + '-'*10)

	def eat(self):
		print('s1.eat' + '-'*10)


class s2(f1):
	
	def show(self):
		print('s2.show' + '-'*10)

	def eat(self):
		print('s2.eat' + '-'*10)


def fcker(obj):
	print(obj.eat())
	print(obj.show())

s1o = s1()
fcker(s1o)

s2o = s2()
fcker(s2o)
