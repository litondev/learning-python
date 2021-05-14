class Player:
	def __init__(self,name,speed):
		self.name = name
		self.speed = speed

	def getName():
		return self.name

	def getSpeed():
		return self.speed

# PalyerIndo(Player,PlayerA)
class PlayerIndo(Player):
	# oppsional/override
	# def __init__(self,name,speed,no):
		# super().__init__(name,speed)
		# or
		# Player.__ini__(self,name,speed)
		# self.no = no

	def setWeton(self,weton):
		self.weton = weton
		return self.weton

	def getName(self):
		return self.name
		
players = PlayerIndo('name',10)

print(players.getName())