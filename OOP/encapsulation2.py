class Human():

	def __init__(self,first,last,age):

		self.first = first
		self.last = last
		if age > 0:
			self._age = age
		else:
			self._age = 0

	@property
	def age(self):
		return self._age


	@age.setter
	def age(self,value):
		if age > 0:
			self._age = value
		else:
			self._age = 0


hum = Human('ankit','dhebar',31)
print(hum.age)


