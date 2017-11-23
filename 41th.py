class cat:
	name = 'cat_jackie'
	color = 'white'

	def run(self):
		print(self.name, '-- is running in the rain!!')


class bosi(cat):

	def setName(self, nn):
		self.name = nn

	def eat(self):
		print(self.name, '-- is eating sanwitch!!')


bs = bosi()

print('bs name is ', bs.name)
print('bs color is ',bs.color)

bs.eat()

bs.setName('cat_Donald')

bs.run()
