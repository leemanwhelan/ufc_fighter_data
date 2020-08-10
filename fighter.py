

class fighter:
	number_of_fighters = 0

	def __init__(self, first_Name, last_Name, height, weight, reach, record):
		self.first_Name = first_Name
		self.last_Name = last_Name
		self.height = height
		self.weight = weight
		self.reach = reach
		self.record = record

	def get_Name(self):
		return (self.first_Name + " " + self.last_Name)

	def describe(self):
		print("Name   : " + self.get_Name())
		print("Height : " + str(self.height[0]) + "'"+ str(self.height[1])+ "\"")
		print("Weight : " + str(self.weight)+ " lbs")
		print("Reach  : " + str(self.reach) + " in")
		print("Record : " + str(self.record[0]) + "-" + str(self.record[1]))

Whittaker = fighter('Robert', 'Whittaker', (5,11), 185, 73, (22, 3))
Whittaker.describe()



