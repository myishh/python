class people:
	country = 'China'

	@classmathod
	def getCountry(cls):
		return cls.country

p = people()
print(p.getCountry())
print(people.getCountry())
