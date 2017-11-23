class F1:
	pass

class S1(F1):
	def show(self):
		print('s1.show')

class S2(F1):
	def show(self):
		print('s2.show')

def func(obj):
	print(obj.show())

s1o = S1()
s2o = S2()

func(s1o)

func(s2o)
