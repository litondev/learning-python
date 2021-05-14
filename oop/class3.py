class Person:

	def __init__ (self,name):
		self.name = name

	def sayHi(self):
		print('Hello There',self.name)

p = Person('Testing')
p.sayHi()