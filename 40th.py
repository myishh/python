class car:
		
	def __init__(self, wn, cl):
		self.wn = wn
		self.cl = cl

	def run(self):
		print('Car is running!')

benz = car(6, 'blue')

print('Car color is %s '%benz.cl)
print('Car wheel num is %d '%benz.wn)

print('-'*30)

class animal():

	def __init__(self):
		print('constructor is being called')

	def __del__(self):
		print('__del__ is being called')

dog = animal()

del dog
