#https://www.geeksforgeeks.org/facade-method-python-design-patterns/
"""Facade pattern with an example of WashingMachine"""

class Washing: 
	'''Subsystem # 1'''
	def wash(self): 
		print("Washing...") 

class SenseLoad: 
	'''Subsystem # 2'''
	def senseWeight(self): 
		print("Sensing load...") 

class Rinsing: 
	'''Subsystem # 2'''
	def rinse(self): 
		print("Rinsing...") 


class Spinning: 
	'''Subsystem # 3'''
	def spin(self): 
		print("Spinning...") 


class WashingMachine: 
	'''Facade'''

	def __init__(self): 
		self.sense = SenseLoad()

		self.washing = Washing() 
		self.rinsing = Rinsing() 
		self.spinning = Spinning() 

	def startWashing(self): 
		self.sense.senseWeight()
		self.sense.senseWeight()
		self.sense.senseWeight()
		self.sense.senseWeight()

		self.washing.wash() 
		# self.sense.senseWeight()
		# self.spinning.spin() 
		self.sense.senseWeight()
		self.rinsing.rinse() 

""" main method """
if __name__ == "__main__": 
	washingMachine = WashingMachine() 
	washingMachine.startWashing() 