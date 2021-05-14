class Player:
	def __init__(self,name,speed):
		self.name = name
		self.speed = speed

	def getName():
		return self.name

	def getSpeed():
		return self.speed

# PalyerInfo(Player,PlayerA)
class PlayerIndo(Player):
	# oppsional/override
	# def __init__(self,name,speed,no):
		# super().__init__(name,speed)
		# Player.__ini__(self,name,speed)
		# self.no = no

	def setAge(self,age):
		self.age = age
		return self.age

	def getName(self):
		return self.name
		
players = PlayerIndo('name',10)
