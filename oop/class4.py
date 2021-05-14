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

	# @info_player.setter
	# def info_play(self,data):
	#	name,age = data.split(' ')
	#	self.name = name
	# 	self.age = age
	# calls => robot_instance.info_player = "hello 50"

	# @property
	#def info_player(self):
	#	return self.name
	# calls => robot_instance.info_palyer

	# @classmethod
	# def generate_info(self):
	#	return cls.job 
	# calls => robot_class.generate_info()

r = Robot()
r.setPopulation()
Robot.howMany()
del r