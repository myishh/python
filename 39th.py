class Car:
	#Attributes
	wheelNum = 2
	color = 'red'

	#Methods
	def getCarInfo(self):
		print('Wheel num : %d, Color : %s'%(self.wheelNum, self.color))

	def run(self):
		print('Car is running')


Benz = Car()

print('Wheen num is %d'%(Benz.wheelNum))
Benz.getCarInfo()
Benz.run()
print('-'*30)

class people:
	__name = 'Tommy'
	__age = 16

	def getName(self):
		return self.__name

	def getAge(self):
		return self.__age

p = people()
print(p.getName(), p.getAge())

print('-'*30)
class Animal:
	
	def setName(self, name):
		self.name = name

	def printName(self):
		print('Name is', self.name)

def myPrint(animalName):
	animalName.printName()

dog1 = Animal()
dog1.setName('Bob')
myPrint(dog1)

cat1 = Animal()
cat1.setName('Benjamin')
myPrint(cat1)
