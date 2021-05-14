class Robot:
	population = 0

	def setPopulation():
		Robot.population += 1

	def __del__(self):
		print('Am Daying')

	def myStaticMethod():
		print("Am Static")

	howMany = staticmethod(myStaticMethod)

	# @staticmethod 
	# def hoMany():
	# 	print('Hai')

r = Robot()
r.setPopulation()
Robot.howMany()
del r