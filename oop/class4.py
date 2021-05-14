class Robot:
	population = 0

	def setPopulation(self):
		# set static
		Robot.population += 1

	def __del__(self):
		print('Am Daying')

	# stati method
	def myStaticMethod():
		print("Am Static")

	howMany = staticmethod(myStaticMethod)

	# also static method
	@staticmethod 
	def getPopulation():
		print(Robot.population)

	# class method
	@classmethod
	def getPopulationClass(cls):
		print(cls.population)

	@property
	def player(self):

		self.name = "my name"
		self.age = 50

		print(f"Name : {self.name} Age : {self.age}")

	@player.setter
	def player(self,data):
		name,age = data.split(' ')

		self.name = name
		self.age = age
		
iRobot = Robot()

iRobot.setPopulation()

Robot.howMany()

Robot.getPopulation()

Robot.getPopulationClass()

iRobot.player = "hello 50"

iRobot.player

del iRobot